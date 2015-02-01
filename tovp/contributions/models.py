from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _
from django.core import exceptions

from model_utils.fields import MonitorField
from model_utils.models import TimeStampedModel
# from dateutil import relativedelta

from contacts.models import Person


class Pledge(TimeStampedModel):
    person = models.ForeignKey(Person, verbose_name="Person", blank=True,
                               related_name='pledges')
    amount = models.DecimalField(_('Amount'), max_digits=20, decimal_places=2)
    amount_paid = models.DecimalField(_('Amount Paid'), max_digits=20,
                                      default=0, decimal_places=2,
                                      null=True, blank=True)
    CURRENCY_CHOICES = (
        ('INR', _('₹')),
        ('USD', _('$')),
        ('EUR', _('€')),
    )
    currency = models.CharField(
        "Currency", max_length=6, choices=CURRENCY_CHOICES, default="INR")
    payments_start_date = models.DateField(
        _("Payments Start"), null=True, blank=True,
        help_text=_('Date of first expected payment for this pledge.'),
    )
    INTERVAL_CHOICES = (
        (u'1', _('1 month')),
        (u'2', _('2 months')),
        (u'3', _('3 months')),
        (u'4', _('4 months')),
        (u'6', _('6 months')),
    )
    interval = models.CharField(
        _("Payments Interval"), max_length=30, choices=INTERVAL_CHOICES,
        help_text=_("Enter planned interval of payments (e.g. 1 month)"),
    )
    STATUS_CHOICES = (
        (u'pending', _('Pending')),
        (u'partial', _('Partially Paid')),
        (u'completed', _('Completed')),
        (u'failed', _('Shadow')),
    )
    status = models.CharField("Status", max_length=30, default='pending',
                              choices=STATUS_CHOICES, blank=True)

    status_changed = MonitorField(monitor='status')

    next_payment_date = models.DateField(
        _("Next Payment Date"), null=True, blank=True,
        help_text=_('Date of next expected payment.'),
    )

    @property
    def progress(self):
        if self.amount_paid and self.amount:
            return self.amount_paid / self.amount * 100
        return 0

    @permalink
    def get_absolute_url(self):
        return ('contributions:pledge:detail', None, {
            'person_id': self.person.pk,
            'pk': self.pk})

    def info(self):
        return 'Pledged {amount}{currency} - {progress}% completed'. \
            format(amount=self.amount, currency=self.get_currency_display(),
                   progress=self.progress, status=self.get_status_display())

    def _calculate_amount_paid(self):
        total = 0
        for contribution in self.contributions.all(). \
                filter(status='completed'):
            total += contribution.amount
        self.amount_paid = total

    # def update_next_payment_due(self):
    #     self.next_payment_date = last_contribution_date + \
    #                              relativedelta(months = self.interval)

    def save(self, **kwargs):
        self._calculate_amount_paid()
        if not self.amount_paid:
            self.status = 'pending'
        elif self.amount_paid < self.amount:
            self.status = 'partial'
        else:
            self.status = 'completed'

        super(Pledge, self).save()

    def __str__(self):
        return '{amount}{currency} ({progress:.2f}%)'.format(
            amount=self.amount, currency=self.get_currency_display(),
            progress=self.progress)


class Contribution(TimeStampedModel):
    pledge = models.ForeignKey(Pledge, verbose_name="Pledge", blank=True,
                               null=True, related_name='contributions')
    person = models.ForeignKey(Person, verbose_name="Person", blank=True,
                               related_name='contributions')
    amount = models.DecimalField(_('Amount'), max_digits=20, decimal_places=2)
    CURRENCY_CHOICES = (
        ('INR', _('₹')),
        ('USD', _('$')),
        ('EUR', _('€')),
    )
    currency = models.CharField(
        "Currency", max_length=6, choices=CURRENCY_CHOICES, default="INR")
    PAYMENT_METHOD_CHOICES = (
        (u'cashl', _('Cash (Indian)')),
        (u'cashf', _('Cash (Foreign)')),
        (u'ccdcsl', _('Credit/Debit Card Swipe Local')),
        (u'ccdcsf', _('Credit/Debit Card Swipe Foreign')),
        (u'neftl', _('NEFT (Indian)')),
        (u'neftf', _('NEFT (Foreign)')),
        (u'chequel', _('Cheque (Indian)')),
        (u'chequef', _('Cheque (Foreign)')),
    )
    payment_method = models.CharField(
        "Payment Method", max_length=16, choices=PAYMENT_METHOD_CHOICES)

    transaction_id = models.CharField(
        _('Transaction ID or Cheque No'), max_length=100, blank=True,
        help_text=_('Transaction ID of this contribution or cheque number.'))

    bank = models.CharField(
        _('Bank'), max_length=100, blank=True,
        help_text=_('Write bank name (and possible branch or location) for cheque'))

    dated = models.DateField(
        _("Dated"), null=True, blank=True,
        help_text=_('Enter date on the cheque')
    )
    cleared_on = models.DateField(
        _("Cleared On"), null=True, blank=True,
        help_text=_('Enter date when transaction was completed '
                    '(money came to TOVP)')
    )
    STATUS_CHOICES = (
        (u'pending', _('Pending')),
        (u'completed', _('Completed')),
        (u'failed', _('Failed')),
    )
    status = models.CharField("Status", max_length=30, choices=STATUS_CHOICES)

    status_changed = MonitorField(monitor='status')

    def __init__(self, *args, **kwargs):
        super(Contribution, self).__init__(*args, **kwargs)
        self._original_pledge = self.pledge

    def clean(self):
        errors = {}

        # Strip all whitespace
        for field in ['transaction_id']:
            if self.__dict__[field]:
                self.__dict__[field] = self.__dict__[field].strip()

        if self.status == 'completed' and not self.cleared_on:
            msg = _("There must be date for completed transaction")
            errors['cleared_on'] = [msg]

        # transaction id is required for cheque or credit/debit cards payments
        if not self.transaction_id:
            if self.payment_method in ['cheque', 'ccdcsl', 'ccdcsf']:
                if self.payment_method in ['ccdcsl', 'ccdcsf']:
                    msg = _("You have to fill Transaction ID for Credit/Debit "
                            "card payment.")
                    errors['transaction_id'] = [msg]
                if self.payment_method == 'cheque':
                    msg = _("You have to fill Cheque Number")
                    errors['transaction_id'] = [msg]
        if errors:
            raise exceptions.ValidationError(errors)

    @property
    def currency_words(self):
        CURRENCY_CHOICES = {
            'INR': 'rupees',
            'USD': 'american dollars',
            'EUR': 'euro',
        }
        return CURRENCY_CHOICES[self.currency]

    @permalink
    def get_absolute_url(self):
        return ('contributions:contribution:detail', None, {
            'person_id': self.person.pk,
            'pk': self.pk})

    def info(self, show_name=None):
        field_values = [
            '#' + str(self.pk),
        ]
        if show_name:
            field_values.append(self.person.full_name)
        field_values.append(str(self.dated))
        field_values.append(str(self.amount))
        field_values.append(self.currency)
        field_values.append('(%s)' % self.get_payment_method_display())
        field_values.append(self.get_status_display())
        return ' - '.join(filter(bool, field_values))

    def save(self, **kwargs):
        super(Contribution, self).save()
        # if contribution pledge changed save original pledge first, so its
        # amount_paid is updated correctly
        if self._original_pledge and (self._original_pledge != self.pledge):
            self._original_pledge.save()
        # save pledge to update its amount_paid
        if self.pledge:
            self.pledge.save()

    def delete(self, **kwargs):
        super(Contribution, self).delete()
        # save pledge to update its amount_paid
        if self.pledge:
            self.pledge.save()

    def __str__(self):
        field_values = (
            self.person.full_name,
            str(self.amount),
            '(%s)' % self.get_payment_method_display()
        )
        return ' - '.join(filter(bool, field_values))
