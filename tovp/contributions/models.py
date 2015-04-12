from datetime import datetime

from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _
from django.core import exceptions

from model_utils.fields import MonitorField
from model_utils.models import TimeStampedModel
# from dateutil import relativedelta
from audit_log.models import AuthStampedModel

from contacts.models import Person
from ananta.models import SourceMixin, NextPrevMixin


class Pledge(TimeStampedModel, AuthStampedModel, NextPrevMixin, SourceMixin):
    def reindex_related(self):
        related = []
        for contribution in self.contributions.all():
            related.append(contribution)
        for promotion in self.assigned_promotions():
            related.append(promotion)
        return related

    person = models.ForeignKey(Person, verbose_name="Person", blank=True,
                               related_name='pledges')
    amount = models.DecimalField(_('Amount'), max_digits=20, decimal_places=2)
    amount_paid = models.DecimalField(_('Amount Paid'), max_digits=20,
                                      default=0, decimal_places=2,
                                      null=True, blank=True)
    CURRENCY_CHOICES = (
        ('INR', _('₹ (INR)')),
        ('USD', _('$ (USD)')),
        ('EUR', _('€ (EUR)')),
        ('GBP', _('£ (GBP)')),
    )
    currency = models.CharField(
        "Currency", max_length=6, choices=CURRENCY_CHOICES, default="INR")
    payments_start_date = models.DateField(
        _("Payments Start"), null=True, blank=True, default=datetime.now,
        help_text=_('Date of first expected payment for this pledge.'),
    )
    INTERVAL_CHOICES = (
        (u'1', _('1 month')),
        (u'2', _('2 months')),
        (u'3', _('3 months')),
        (u'4', _('4 months')),
        (u'6', _('6 months')),
        (u'12', _('12 months')),
    )
    interval = models.CharField(
        _("Payments Interval"), max_length=30, choices=INTERVAL_CHOICES,
        default=u'1', help_text=_("Enter planned interval of payments "
                                  "(e.g. 1 month)"),
    )
    number_of_instalments = models.IntegerField(
        _('Number of instalments'), default=1,
        help_text=_('If somebody knows in how many instalment they would like '
                    'to pay the pledge.'))
    STATUS_CHOICES = (
        (u'pending', _('Pledged')),
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

    cache_assigned_promotions = None

    def assigned_promotions(self):
        """
        Returns all promotions (e.g. Golden Brick, Silver Coin) for person
        """
        if not self.cache_assigned_promotions:
            from promotions.models import promotions
            assigned_promotions = []
            for promotion_class in promotions:
                for promotion in promotion_class.objects.all(). \
                        filter(pledge=self):
                    assigned_promotions.append(promotion)
            self.cache_assigned_promotions = assigned_promotions
        return self.cache_assigned_promotions

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
        return 'Pledged {amount}{currency} - {progress:.2f}% completed'. \
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


class Contribution(TimeStampedModel, AuthStampedModel, NextPrevMixin, SourceMixin):
    pledge = models.ForeignKey(Pledge, verbose_name="Pledge",
                               related_name='contributions')

    # fields to save serial number for contributions for which are not from
    # the books/slips and we should generate receipt for
    serial_year = models.CharField(
        _('Serial Number Year'), max_length=5, blank=True,
        help_text=_('Serial Number Year of this contribution.'))
    serial_number = models.CharField(
        _('Serial Number'), max_length=5, blank=True,
        help_text=_('Serial Number of this contribution for financial year.'))

    amount = models.DecimalField(_('Amount'), max_digits=20, decimal_places=2)
    CURRENCY_CHOICES = (
        ('INR', _('₹ (INR)')),
        ('USD', _('$ (USD)')),
        ('EUR', _('€ (EUR)')),
        ('GBP', _('£ (GBP)')),
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
        (u'paypal', _('Paypal')),
        (u'axis', _('Gateway Axis (Internet)')),
    )
    payment_method = models.CharField(
        "Payment Method", max_length=16, choices=PAYMENT_METHOD_CHOICES)

    transaction_id = models.CharField(
        _('Transaction ID or Cheque No'), max_length=100, blank=True,
        help_text=_('Transaction ID of this contribution or cheque number.'))

    bank = models.CharField(
        _('Bank'), max_length=100, blank=True,
        help_text=_('Write bank name (and possible branch or location) '
                    'for cheque'))

    dated = models.DateField(
        _("Dated"), null=True, blank=True,
        help_text=_('Enter date on the cheque')
    )
    receipt_date = models.DateField(
        _("Receipt Date"), null=True, blank=True,
        help_text=_("Enter date which should be on the receipt.")
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

    book_number = models.CharField(
        _('Book Number'), max_length=20, blank=True,
        help_text=_('Enter if you are entering contribution from book'))

    slip_number = models.CharField(
        _('Slip Number'), max_length=20, blank=True,
        help_text=_('Enter if you are entering contribution from slip'))

    overwrite_name = models.CharField(
        _("Name who pays on behalf of main contact"), max_length=255,
        blank=True)
    overwrite_address = models.CharField(
        _("Address who pays on behalf of main contact"), max_length=255,
        blank=True)

    is_external = models.BooleanField(
        _('Non Mayapur TOVP receipt'), default=False, db_index=True,
        help_text='This MUST be checked if other than India TOVP receipt '
                  'was given.')

    def __init__(self, *args, **kwargs):
        super(Contribution, self).__init__(*args, **kwargs)
        if self.serial_year:
            self._serial_year = self.serial_year
            self._serial_number = self.serial_number
        else:
            self._serial_year = None
            self._serial_number = None

        if self.pk:
            self._original_pledge = self.pledge
        else:
            self._original_pledge = None

    def get_serial_number(self):
        if self.book_number:
            return '{book}/{slip}'.format(book=self.book_number,
                                          slip=self.slip_number)
        elif self.serial_year and self.serial_number:
            number = '%05d' % int(self.serial_number)
            if self.status == 'completed':
                prefix = 'TOVP'
            else:
                prefix = 'TMP'
            return '{prefix}/{year}/{number}'.format(prefix=prefix,
                                                     year=self.serial_year,
                                                     number=number)
        return ''

    def generate_serial_year(self):
        if self.receipt_date:
            date = self.receipt_date
            if date.month < 4:
                year = date.year - 2001
            else:
                year = date.year - 2000
            return '%d-%d' % (year, year + 1)

    def clean(self):
        errors = {}

        # Strip all whitespace
        for field in ['transaction_id']:
            if self.__dict__[field]:
                self.__dict__[field] = self.__dict__[field].strip()

        if self.status == 'completed' and not self.cleared_on:
            msg = _("There must be date for completed transaction")
            errors['cleared_on'] = [msg]

        if (not (self.receipt_date or self.cleared_on) and
                self.payment_method != 'paypal'):
            msg = _("You have to fill this when there is no Cleared On date.")
            errors['receipt_date'] = [msg]

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

        self.ensure_book_and_slip_number()
        self.ensure_serial_number_not_generated()

        if errors:
            raise exceptions.ValidationError(errors)

    def ensure_book_and_slip_number(self):
        """
        Make sure that none or both book and slip number is entered
        """
        if bool(self.book_number) != bool(self.slip_number):
            msg = _("There must be both book number and slip number")
            if self.book_number:
                raise exceptions.ValidationError({'slip_number': [msg]})
            else:
                raise exceptions.ValidationError({'book_number': [msg]})

    def ensure_serial_number_not_generated(self):
        if self._serial_number and self.book_number:
            msg = _("This contribution has already serial number generated, "
                    "You cannot add book and slip numbers anymore.")
            raise exceptions.ValidationError({'book_number': [msg]})
        if self._serial_number and self.is_external:
            msg = _("This contribution has already serial number generated, "
                    "You cannot set is as external anymore.")
            raise exceptions.ValidationError({'is_external': [msg]})

    @property
    def currency_words(self):
        CURRENCY_CHOICES = {
            'INR': 'rupees',
            'USD': 'american dollars',
            'EUR': 'euro',
            'GBP': 'british pounds',
        }
        return CURRENCY_CHOICES[self.currency]

    @permalink
    def get_absolute_url(self):
        return ('contributions:contribution:detail', None, {
            'person_id': self.pledge.person.pk,
            'pk': self.pk})

    def info(self, show_name=None):
        field_values = [
            '#' + str(self.pk),
        ]
        if show_name:
            field_values.append(self.person.full_name)
        # field_values.append(str(self.dated))
        field_values.append(str(self.amount))
        field_values.append(self.currency)
        field_values.append('(%s)' % self.get_payment_method_display())
        field_values.append(self.get_status_display())
        return ' - '.join(filter(bool, field_values))

    def save(self, **kwargs):
        if self.cleared_on and not self.receipt_date:
            self.receipt_date = self.cleared_on
        if not self.receipt_date:
            if self.pk:
                self.receipt_date = self.created
            else:
                self.receipt_date = datetime.now()

        if self._serial_year:
            self.serial_year = self._serial_year
            self.serial_number = self._serial_number

        if not (self.is_external or self.book_number or self.serial_number):
            if self.receipt_date:
                date = self.receipt_date
                year = date.year
                if date.month < 4:
                    year -= 1
                print(year > 2014, year)
                if year > 2014:
                    self.serial_year = self.generate_serial_year()
                    self.serial_number = len(
                        Contribution.objects.all().
                        filter(serial_year=self.serial_year)) + 1

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
            self.pledge.person.full_name,
            str(self.amount),
            '(%s)' % self.get_payment_method_display()
        )
        return ' - '.join(filter(bool, field_values))
