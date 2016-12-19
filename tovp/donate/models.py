from django.db import models
# from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel
from audit_log.models import AuthStampedModel

from contacts.models import Person
from ananta.models import NextPrevMixin
from currencies.utils import get_currency_choices


class WebDonation(TimeStampedModel, AuthStampedModel, NextPrevMixin):
    csrf_token = models.CharField(
        max_length=100, blank=True,
        help_text=_('CSRF Token is used to identify re-submit records.'))
    first_name = models.CharField(
        max_length=100, blank=True,
        help_text=_('Enter your first name.'))
    middle_name = models.CharField(
        max_length=100, blank=True,
        help_text=_('Enter your middle name.'))
    last_name = models.CharField(
        max_length=100, blank=True,
        help_text=_('Enter your surname.'))
    initiated_name = models.CharField(
        max_length=100, blank=True,
        help_text=_('Spiritual name if you have e.g: Krishna Das, Tulasi Dasi, '
                    'Bhakta Burfi')
    )
    address = models.TextField(_("Address"), blank=True)
    email = models.EmailField("Email", max_length=200, blank=True)
    phone_number = models.CharField(
        max_length=100, blank=True,
        help_text='Enter your phone number. If it is a non-Indian number '
                  'please use the international format e.g.: +421 222 333 444')

    # pan_card_number for indians

    amount = models.DecimalField(_('Amount'), max_digits=20, decimal_places=2)
    currency = models.CharField(
        "Currency", max_length=6, choices=get_currency_choices(), default="INR")
    number_of_instalments = models.IntegerField(_('Number of instalments'), default=1)

    person = models.ForeignKey(Person, verbose_name="Person", blank=True,
                               related_name='web_donations')

    # @permalink
    # def get_absolute_url(self):
    #     return ('donate:web_donation:detail', None, {
    #         'pk': self.pk})

    # def info(self):
    #     return 'Pledged {amount}{currency} - {progress:.2f}% completed'. \
    #         format(amount=self.amount, currency=self.get_currency_display(),
    #                progress=self.progress, status=self.get_status_display())

    def save(self, **kwargs):
        super(WebDonation, self).save()

    def __str__(self):
        return '{amount}{currency}'.format(
            amount=self.amount, currency=self.get_currency_display())
