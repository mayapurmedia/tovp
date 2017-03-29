from datetime import datetime

from django.conf import settings
from django.core import exceptions
from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _
from django.utils.functional import cached_property

from model_utils.fields import MonitorField
from model_utils.models import TimeStampedModel
from dateutil.relativedelta import relativedelta
from audit_log.models import AuthStampedModel

from contacts.models import Person
from ananta.models import SourceMixin, NextPrevMixin
from currencies.utils import (get_currency_choices, get_currency_words,
                              get_foreign_currency_choices)


class Pledge(TimeStampedModel, AuthStampedModel, NextPrevMixin, SourceMixin):
    """
    Through Pledge model you can keep track of all its contributions and
    associated promotions. Contribution and promotions cannot exist without its
    pledge.
    """
    NEXT_PAYMENT_GRACE_PERIOD = 14

    def reindex_related(self):
        """
        Function which returns list models to be reindex when model is updated.
        """
        related = []
        for contribution in self.contributions.all():
            related.append(contribution)
        for promotion in self.assigned_promotions:
            related.append(promotion)
        return related

    # Foreign key to Person (Contact)
    person = models.ForeignKey(Person, verbose_name="Person", blank=True,
                               related_name='pledges')

    # Foreign key for user who is assigned for Follow Up of this Pledge
    followed_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                                    blank=True, related_name='pledges')

    amount = models.DecimalField(_('Amount'), max_digits=20, decimal_places=2)
    amount_paid = models.DecimalField(_('Amount Paid'), max_digits=20,
                                      default=0, decimal_places=2,
                                      null=True, blank=True)
    currency = models.CharField("Currency", max_length=6,
                                choices=get_currency_choices(), default="INR")

    # Date from which person supose to start pay for this pledge. Help us to
    # recognize which pledge is late with payments. Is for example used as
    # filter on Follow Up page.
    payments_start_date = models.DateField(
        _("Payments Start"), null=True, blank=True, default=datetime.now,
        help_text=_('Date of first expected payment for this pledge.'),
    )

    # Interval helps us to determine expected date of next payment
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

    # Todo: Number of instalments - Currently doesn't do anything.
    number_of_instalments = models.IntegerField(
        _('Number of instalments'), default=1,
        help_text=_('If somebody knows in how many instalment they would like '
                    'to pay the pledge.'))

    # Status of the pledge
    STATUS_CHOICES = (
        # New pledge without any payments
        (u'pending', _('Pledged')),
        # Pledge is partialy paid (0% > paid <100%)
        (u'partial', _('Partially Paid')),
        # Fully paid pledge (paid >= 100%)
        (u'completed', _('Completed')),
        (u'failed', _('Shadow')),
        (u'canceled', _('Canceled')),
    )
    status = models.CharField("Status", max_length=30, default='pending',
                              choices=STATUS_CHOICES, blank=True)

    # Keeps track when Status field got changed
    status_changed = MonitorField(monitor='status')

    # Expected date for next payment
    next_payment_date = models.DateField(
        _("Next Payment Date"), null=True, blank=True,
        help_text=_('Date of next expected payment.'),
    )

    @cached_property
    def assigned_promotions(self):
        """
        Returns all promotions (e.g. Golden Brick, Silver Coin) for person
        """
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
        """
        Return pledge's payment progress in percents.  
        """
        if self.amount_paid and self.amount:
            return self.amount_paid / self.amount * 100
        return 0

    @permalink
    def get_absolute_url(self):
        return ('contributions:pledge:detail', None, {
            'person_id': self.person.pk,
            'pk': self.pk})

    def info(self):
        """
        Generates one line summary about pledge
        """
        return 'Pledged {amount}{currency} - {progress:.2f}% completed'. \
            format(amount=self.amount, currency=self.get_currency_display(),
                   progress=self.progress, status=self.get_status_display())

    def _calculate_amount_paid(self):
        """
        Calculates how much of pledge is paid.
        """
        total = 0
        for contribution in self.contributions.all(). \
                filter(status='completed'):
            total += contribution.amount
        self.amount_paid = total

    def update_next_payment_date(self):
        """
        Update pledge's next_payment_date based on latest contribution and
        payment interval plus grace period (NEXT_PAYMENT_GRACE_PERIOD).  
        """
        latest = self.contributions.all().order_by('-cleared_on')[:1]
        interval = int(self.interval)
        # if there is any contribution dated after payment start
        if latest.count() and latest[0].cleared_on and (latest[0].cleared_on > self.payments_start_date):
            self.next_payment_date = latest[0].cleared_on + \
                relativedelta(months=interval)
        else:
            self.next_payment_date = self.payments_start_date + \
                relativedelta(months=interval) + \
                relativedelta(days=self.NEXT_PAYMENT_GRACE_PERIOD)
        return self.next_payment_date

    def has_late_payment(self):
        """
        Returns True if pledge is in late payment 
        """
        self.update_next_payment_date()
        if self.next_payment_date > datetime.date(datetime.now()):
            return False
        return True

    def save(self, **kwargs):
        self._calculate_amount_paid()
        # set pledge's status depending on ammount paid
        if not self.amount_paid:
            self.status = 'pending'
        elif self.amount_paid < self.amount:
            self.status = 'partial'
        else:
            self.status = 'completed'

        # set next payment should be expected
        self.update_next_payment_date()
        super(Pledge, self).save()

    def __str__(self):
        return '{amount}{currency} ({progress:.2f}%)'.format(
            amount=self.amount, currency=self.get_currency_display(),
            progress=self.progress)

    def can_user_delete(self, user):
        """
        Check if user is able to delete the pledge. Some users can delete any 
        pledge, some for safety can delete only pledges which has no assigned 
        contributions.
        """
        if user.has_perm('contributions.delete_pledge'):
            return True
        if (user.has_perm('contributions.can_delete_if_no_contributions') and
                not self.contributions.all().count()):
            return True
        return False

    def assign_follow_up(self, user):
        """
        Assigns user for Follow Up of the pledge or unset follow up if followed
        by other user.
        """
        if not (self.followed_by and self.followed_by != user):
            if self.followed_by:
                self.followed_by = None
            else:
                self.followed_by = user
            self.save()

    class Meta:
        permissions = (("can_delete_if_no_contributions",
                        "Can delete if no contributions"),)


class BaseContributionMixin(TimeStampedModel, AuthStampedModel, NextPrevMixin,
                            SourceMixin):
    """
    Mixin to define base fields which can be shared for Contributions and 
    BulkPayments.
    """
    # fields to save serial number for contributions for which are not from
    # the books/slips and we should generate receipt for
    serial_year = models.CharField(
        _('Serial Number Year'), max_length=5, blank=True,
        help_text=_('Serial Number Year of this contribution.'))
    serial_number = models.CharField(
        _('Serial Number'), max_length=5, blank=True,
        help_text=_('Serial Number of this contribution for financial year.'))

    # serial_number_int = models.IntegerField(
    #     _('Serial Number Int'), null=True, blank=True, default=None,
    #     help_text=_('Serial Number of this contribution for financial year.'))

    amount = models.DecimalField(_('Amount'), max_digits=20, decimal_places=2)
    currency = models.CharField(
        "Currency", max_length=6, choices=get_currency_choices(), default="INR")

    # Whenever is cash coming from foreign currency (other than INR) we note
    # it here for reference
    foreign_amount = models.DecimalField(_('Foreign Amount'), max_digits=20,
                                         decimal_places=2, blank=True,
                                         null=True)
    foreign_currency = models.CharField(
        "Foreign Currency", max_length=6, choices=get_foreign_currency_choices(),
        default="INR", help_text=_('Please fill if donation is coming from'
                                   'foreign currency.'))

    PAYMENT_METHOD_CHOICES = (
        (u'cashl', _('Cash (Indian)')),
        (u'cashf', _('Cash (Foreign)')),
        (u'cashd', _('Cash Deposit')),
        (u'ccdcsl', _('Credit/Debit Card Swipe Local')),
        (u'ccdcsf', _('Credit/Debit Card Swipe Foreign')),
        (u'neftl', _('NEFT (Indian)')),
        (u'neftf', _('NEFT/Bank Transfer (Foreign)')),
        (u'chequel', _('Cheque (Indian)')),
        (u'chequef', _('Cheque (Foreign)')),
        (u'chequed', _('Cheque Deposit')),
        (u'paypal', _('Paypal')),
        (u'axis', _('Gateway Axis (Internet)')),
        (u'treasury', _('ISKCON Treasury')),
        (u'bulk', _('Part of the Bulk Payment')),
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
        (u'canceled', _('Canceled')),
    )
    status = models.CharField("Status", max_length=30, choices=STATUS_CHOICES)
    status_changed = MonitorField(monitor='status')

    # If contribution is entered from receipt book we enter book number
    book_number = models.CharField(
        _('Book Number'), max_length=20, blank=True,
        help_text=_('Enter if you are entering contribution from book'))
    # and slip number
    slip_number = models.CharField(
        _('Slip Number'), max_length=20, blank=True,
        help_text=_('Enter if you are entering contribution from slip'))

    # If contribution is paid on behalf of somebody we may need to overwrite
    # any of name, address, PAN card to show on receipt instead of Contact
    overwrite_name = models.CharField(
        _("Name who pays on behalf of main contact"), max_length=255,
        blank=True)
    overwrite_address = models.CharField(
        _("Address who pays on behalf of main contact"), max_length=255,
        blank=True)
    overwrite_pan_card = models.CharField(
        _('Overwrite PAN card number'), max_length=50, blank=True, null=True)

    note = models.TextField(_("Note"), max_length=255, blank=True)

    def __init__(self, *args, **kwargs):
        super(BaseContributionMixin, self).__init__(*args, **kwargs)
        if self.serial_year:
            self._serial_year = self.serial_year
            self._serial_number = self.serial_number
        else:
            self._serial_year = None
            self._serial_number = None

    @classmethod
    def get_serial_number_prefix(cls, completed=None):
        """
        Generates serial_number_prefix based on variables from Model class
        """
        if completed:
            return cls.serial_number_prefix_completed
        return cls.serial_number_prefix_temporary

    def get_serial_number(self):
        """
        Generates full serial number.
        """
        if self.book_number:
            return '{book}/{slip}'.format(book=self.book_number,
                                          slip=self.slip_number)
        elif self.serial_year and self.serial_number:
            number = '%05d' % int(self.serial_number)
            if self.status == 'completed':
                prefix = self.get_serial_number_prefix(completed=True)
            else:
                prefix = self.get_serial_number_prefix(completed=None)

            atg = ''
            if self.status == 'completed' and self.overwrite_pan_card != 'hide' and (self.overwrite_pan_card or self.pledge.person.pan_card_number):
                atg = '80G/'
            return '{prefix}/{year}/{atg}{number}'.format(prefix=prefix,
                                                          year=self.serial_year,
                                                          atg=atg,
                                                          number=number)
        return ''

    def generate_serial_year(self):
        """
        Serial number year is generated based on India financial year.
        E.g. April - March
        """
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

    @property
    def currency_words(self):
        return get_currency_words(self.currency)

    def info(self, show_name=None):
        """
        Generates one line summary
        """
        field_values = [
            '#' + str(self.pk),
            str(self.amount),
            self.currency,
            '(%s)' % self.get_payment_method_display(),
            self.get_status_display()
        ]
        return ' - '.join(filter(bool, field_values))

    def save(self, **kwargs):
        if self.cleared_on and not self.receipt_date:
            self.receipt_date = self.cleared_on
            print(self.receipt_date)
        if not self.receipt_date:
            if self.pk:
                self.receipt_date = self.created
            else:
                self.receipt_date = datetime.now()

        if self._serial_year:
            self.serial_year = self._serial_year
            self.serial_number = self._serial_number

        super(BaseContributionMixin, self).save()

    class Meta:
        abstract = True


class BulkPayment(BaseContributionMixin):
    """
    BulkPayment is used for collectors, like when somebody brings cash for
    multiple people, or make bank transfer on behalf of other people.
    """
    person = models.ForeignKey(Person, verbose_name="Person", blank=True,
                               related_name='bulk_payments')

    # There are two types of receipts:
    #
    # Official receipt: collector gets official receipt which can be used for
    # accounting purposes. Donors under such bulk payment will not be able to
    # receive official receipts, only aknowledgement. Official receipts will be
    # used most probably for everything else then cash.
    #
    # (e.g.: Collector transfers 1,00,000 by bank on behalf of 2 donors of 50000
    # each. Collector gets official receipt based on bank tranfer and thus
    # individual donors cannot get official receipt anymore)
    #
    # Aknowldgement: confirmation for collector that he gave funds to us on
    # behalf of donors, but it cannot be used for accounting purposes as each
    # donor under bulk payment will get own official receipt.
    #
    # (e.g: Collector brings 1,00,000 in cash on behalf of 2 donors of 50000
    # each. Collector gets aknowledgement so he has prove he gave cash to us,
    # but he cannot use it in his accounting for tax benefits, and we generate
    # official receipts for both of donors for 50000 each which they can than
    # use in their accounting)
    RECEIPT_TYPE_CHOICES = (
        ('official', _('Official')),
        ('acknowledgement', _('Not official / Acknowledgement')),
    )
    receipt_type = models.CharField(
        "Receipt Type", max_length=100, choices=RECEIPT_TYPE_CHOICES)

    def get_serial_number_prefix(self, completed=None):
        """
        Generated serial_number_prefix based on receipt type and status of the
        payment
        """
        if self.receipt_type == 'official':
            if completed:
                return 'BULK-TOVP'
            return 'BULK-TMP'
        else:
            return 'BULK-INTRA'

    def get_deposit_status(self):
        """
        Generates info of how many associated contributions are deposited.
        Is used for cash.
        """
        status = ''
        deposited = 0
        not_deposited = 0
        for contribution in self.contributions.all():
            if contribution.deposited_status == 'deposited':
                deposited += 1
            else:
                not_deposited += 1
            if deposited and not not_deposited:
                status = 'success'
            else:
                status = 'danger'
        return '<div class="btn btn-%s btn-xs">%d of %d deposited</div>' % (status, deposited, deposited + not_deposited)

    @permalink
    def get_absolute_url(self):
        return ('contributions:bulk_payment:detail', None, {
            'person_id': self.person.pk,
            'pk': self.pk})

    def get_serial_number(self):
        """
        Generates full serial number.
        """
        if self.book_number:
            return '{book}/{slip}'.format(book=self.book_number,
                                          slip=self.slip_number)
        elif self.serial_year and self.serial_number:
            number = '%05d' % int(self.serial_number)
            if self.status == 'completed':
                prefix = self.get_serial_number_prefix(completed=True)
            else:
                prefix = self.get_serial_number_prefix(completed=None)

            atg = ''
            if self.status == 'completed' and self.overwrite_pan_card != 'hide' and (self.overwrite_pan_card or self.person.pan_card_number):
                atg = '80G/'
            return '{prefix}/{year}/{atg}{number}'.format(prefix=prefix,
                                                          year=self.serial_year,
                                                          atg=atg,
                                                          number=number)
        return ''

    def ensure_serial_number_not_generated(self):
        """
        Used for validation. Once contribution have serial number, we cannot
        change and use book and slip number. It is done like this to ensure
        there are no missing serial numbers/receipts for audit and to make sure
        that after giving receipt to donor we have same serial in our database.
        """
        if self._serial_number and self.book_number:
            msg = _("This contribution has already serial number generated, "
                    "You cannot add book and slip numbers anymore.")
            raise exceptions.ValidationError({'book_number': [msg]})

    def __str__(self):
        field_values = (
            '#' + str(self.pk),
            self.person.mixed_name,
            str(self.amount),
            str(self.receipt_date),
            # '(%s)' % self.get_payment_method_display()
        )
        return ' - '.join(filter(bool, field_values))

    def save(self, **kwargs):
        if not (self.book_number or self.serial_number):
            if self.receipt_date:
                date = self.receipt_date
                year = date.year
                if date.month < 4:
                    year -= 1
                if year > 2014:
                    self.serial_year = self.generate_serial_year()
                    self.serial_number = len(
                        self.__class__.objects.all().
                        filter(receipt_type=self.receipt_type).
                        filter(serial_year=self.serial_year)) + 1

        super(BulkPayment, self).save()


class Contribution(BaseContributionMixin):
    """
    Contribution is used for individual contributions for donors.
    """
    serial_number_prefix_completed = 'TOVP'
    serial_number_prefix_temporary = 'TMP'

    # Foreign key to pledge
    pledge = models.ForeignKey(Pledge, verbose_name="Pledge",
                               related_name='contributions')

    # We have various receipt types:
    #
    # Mayapur Receipt: for transaction in India where Mayapur TOVP office gives
    # official receipt which can be used for accounting purposes/tax deduction
    # in India.
    #
    # USA Receipt: for transaction which comes through USA office, can be used
    # for accounting purposes/tax decuction in USA.
    #
    # External Receipt: for any transactions where receipt is given by others
    # then above two.
    #
    # Examples for external receipts:
    # - when official receipt was given by ISKCON Tirupati, we cannot produce
    # another official receipt here as there would be duplicate donation with
    # only one payment
    # - when contribution is part of bulk payment (with Official receipt),
    # e.g: when collector transfered payment by bank so he is one who got
    # official receipt and individual donors for each contribution cannot get
    # official receipt anymore only aknowledgement
    RECEIPT_TYPE_CHOICES = (
        ('mayapur-receipt', _('Mayapur Receipt')),
        ('usa-receipt', _('USA Receipt')),
        ('external-receipt', _('External / Non Receipt')),
    )
    receipt_type = models.CharField(
        "Receipt Type", max_length=100, choices=RECEIPT_TYPE_CHOICES,
        default='external-receipt',
    )

    collector = models.ForeignKey(
        Person, verbose_name="Collector", blank=True, null=True,
        related_name='collector_contributions',
        help_text='If this is comes through collector.')

    # In case contribution is part of bulk payment we will use foreign key to
    # specific bulk payment
    bulk_payment = models.ForeignKey(
        BulkPayment, verbose_name="Bulk Payment", blank=True, null=True,
        related_name='contributions',
        help_text=_('If this contribution is part of bulk payment please choose'
                    'it here.'))

    # Keeps track of deposited status, where first logical state is
    # 'Not deposited' and final state is 'Deposited'. Is used to keep track
    # which cash transactions needs to be deposited in treasury
    DEPOSITED_STATUS_CHOICES = (
        ('not-deposited', _('Not deposited')),
        ('ready-to-deposit', _('Ready to deposit')),
        ('deposited', _('Deposited')),
    )
    deposited_status = models.CharField(
        "Is Deposited", max_length=20, choices=DEPOSITED_STATUS_CHOICES,
        default="not-deposited")
    deposited_status_changed = MonitorField(monitor='deposited_status')

    # Deposited status flow used by widget for changing status state.
    DEPOSITED_STATUS_FLOW = {
        'not-deposited': 'ready-to-deposit',
        'ready-to-deposit': 'deposited',
        'deposited': 'not-deposited',
    }

    def info(self, show_name=None):
        field_values = [
            '#' + str(self.pk),
            self.receipt_date.strftime("%B %-d, %Y"),
            str(self.amount),
            self.currency,
            '(%s)' % self.get_payment_method_display(),
            self.get_status_display()
        ]
        if self.bulk_payment:
            field_values.append('[%s]' % self.get_deposited_status_display())
        return ' - '.join(filter(bool, field_values))

    def change_deposited_status(self, user):
        """
        Changes deposit status if user us capable to do so based on permissions.
        """
        next_status = self.DEPOSITED_STATUS_FLOW[self.deposited_status]
        if next_status == 'deposited':
            if user.has_perm('contributions.can_deposit'):
                self.deposited_status = next_status
            else:
                self.deposited_status = 'not-deposited'

        if next_status == 'ready-to-deposit':
                self.deposited_status = next_status

        if next_status == 'not-deposited':
            if user.has_perm('contributions.can_deposit'):
                self.deposited_status = next_status

        self.save()

    # todo: seems it is possible to remove is_external from everythere as
    # it is replaced receipt type
    is_external = models.BooleanField(
        _('Non Mayapur TOVP receipt'), default=False, db_index=True,
        help_text='This MUST be checked if other than India TOVP receipt '
                  'was given.')

    def __init__(self, *args, **kwargs):
        super(Contribution, self).__init__(*args, **kwargs)
        if self.pk:
            self._original_pledge = self.pledge
        else:
            self._original_pledge = None

    def reindex_related(self):
        """
        Function which returns list models to be reindex when model is updated.
        """
        related = []
        if self.bulk_payment:
            related.append(self.bulk_payment)
        return related

    def ensure_serial_number_not_generated(self):
        if self._serial_number and self.book_number:
            msg = _("This contribution has already serial number generated, "
                    "You cannot add book and slip numbers anymore.")
            raise exceptions.ValidationError({'book_number': [msg]})
        if self._serial_number and self.receipt_type == 'external-receipt':
            msg = _("This contribution has already serial number generated, "
                    "You cannot set is as external anymore.")
            raise exceptions.ValidationError({'receipt_type': [msg]})

    @permalink
    def get_absolute_url(self):
        return ('contributions:contribution:detail', None, {
            'person_id': self.pledge.person.pk,
            'pk': self.pk})

    def save(self, **kwargs):
        # set contribution to external if bulk payment is official receipt type
        if self.bulk_payment and self.bulk_payment.receipt_type == 'official':
            self.receipt_type = 'external-receipt'

        if (self.receipt_type == 'mayapur-receipt'
                and not (self.book_number or self.serial_number)):
            if self.receipt_date:
                date = self.receipt_date
                year = date.year
                if date.month < 4:
                    year -= 1
                if year > 2014:
                    self.serial_year = self.generate_serial_year()
                    last_serial = 0
                    try:
                        last_serial = self.__class__.objects.all(). \
                            filter(serial_year=self.serial_year). \
                            order_by('-created')[0].serial_number
                    except:
                        pass

                    self.serial_number = str(int(last_serial) + 1)

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

    class Meta:
        permissions = (("can_edit_completed", "Can edit completed"),
                       ("can_change_deposit_status", "Can change deposit status"),
                       ("can_do_follow_up", "Can do follow up"),
                       ("can_deposit", "Can mark as deposited"),
                       ("can_move_contribution", "Can move contribution"))


class FollowUp(TimeStampedModel, AuthStampedModel):
    """
    Keep track of follow ups. After any contact with donor during follow up
    we should create new follow up, so others can see history of any follow up. 
    """
    pledge = models.ForeignKey(Pledge, verbose_name="Pledge",
                               related_name='follow_ups')

    STATUS_CHOICES = (
        ('wrong-contact', _('Wrong contact')),
        ('could-not-reach', _('Could not reach')),
        ('waiting-reply', _('Waiting for reply')),
        ('agreed-to-pay', _('Agreed to pay')),
        ('see-note', _('See note')),
        ('will-not-pay', _('Will not pay')),
    )
    status = models.CharField("Status", max_length=30, choices=STATUS_CHOICES)
    note = models.TextField(_("Note"), blank=True)

    @permalink
    def get_absolute_url(self):
        return ('contributions:follow_up:detail', None, {
            'pledge_id': self.pledge.pk,
            'pk': self.pk})
