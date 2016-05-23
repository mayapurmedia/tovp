import datetime
import re

from django.conf import settings
from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _, pgettext_lazy as __
from django.core import exceptions
from django.apps import apps

from django.core.validators import RegexValidator

from django_countries.fields import CountryField

from model_utils.models import TimeStampedModel
from audit_log.models import AuthStampedModel

from ananta.models import NextPrevMixin


class Person(AuthStampedModel, NextPrevMixin, TimeStampedModel):
    def reindex_related(self):
        related = []
        for pledge in self.pledges.all():
            related.append(pledge)
        return related

    # title of the person
    MR, MISS, MRS, MS, DR = ('Mr', 'Miss', 'Mrs', 'Ms', 'Dr')
    TITLE_CHOICES = (
        (MR, _("Mr")),
        (MISS, _("Miss")),
        (MRS, _("Mrs")),
        (MS, _("Ms")),
        (DR, _("Dr")),
    )

    # Regex for each country. Not listed countries don't use postcodes
    # Based on http://en.wikipedia.org/wiki/List_of_postal_codes
    POSTCODES_REGEX = {
        'AC': r'^[A-Z]{4}[0-9][A-Z]$',
        'AD': r'^AD[0-9]{3}$',
        'AF': r'^[0-9]{4}$',
        'AI': r'^AI-2640$',
        'AL': r'^[0-9]{4}$',
        'AM': r'^[0-9]{4}$',
        'AR': r'^([0-9]{4}|[A-Z][0-9]{4}[A-Z]{3})$',
        'AS': r'^[0-9]{5}(-[0-9]{4}|-[0-9]{6})?$',
        'AT': r'^[0-9]{4}$',
        'AU': r'^[0-9]{4}$',
        'AX': r'^[0-9]{5}$',
        'AZ': r'^AZ[0-9]{4}$',
        'BA': r'^[0-9]{5}$',
        'BB': r'^BB[0-9]{5}$',
        'BD': r'^[0-9]{4}$',
        'BE': r'^[0-9]{4}$',
        'BG': r'^[0-9]{4}$',
        'BH': r'^[0-9]{3,4}$',
        'BL': r'^[0-9]{5}$',
        'BM': r'^[A-Z]{2}([0-9]{2}|[A-Z]{2})',
        'BN': r'^[A-Z}{2}[0-9]]{4}$',
        'BO': r'^[0-9]{4}$',
        'BR': r'^[0-9]{5}(-[0-9]{3})?$',
        'BT': r'^[0-9]{3}$',
        'BY': r'^[0-9]{6}$',
        'CA': r'^[A-Z][0-9][A-Z][0-9][A-Z][0-9]$',
        'CC': r'^[0-9]{4}$',
        'CH': r'^[0-9]{4}$',
        'CL': r'^([0-9]{7}|[0-9]{3}-[0-9]{4})$',
        'CN': r'^[0-9]{6}$',
        'CO': r'^[0-9]{6}$',
        'CR': r'^[0-9]{4,5}$',
        'CU': r'^[0-9]{5}$',
        'CV': r'^[0-9]{4}$',
        'CX': r'^[0-9]{4}$',
        'CY': r'^[0-9]{4}$',
        'CZ': r'^[0-9]{5}$',
        'DE': r'^[0-9]{5}$',
        'DK': r'^[0-9]{4}$',
        'DO': r'^[0-9]{5}$',
        'DZ': r'^[0-9]{5}$',
        'EC': r'^EC[0-9]{6}$',
        'EE': r'^[0-9]{5}$',
        'EG': r'^[0-9]{5}$',
        'ES': r'^[0-9]{5}$',
        'ET': r'^[0-9]{4}$',
        'FI': r'^[0-9]{5}$',
        'FK': r'^[A-Z]{4}[0-9][A-Z]{2}$',
        'FM': r'^[0-9]{5}(-[0-9]{4})?$',
        'FO': r'^[0-9]{3}$',
        'FR': r'^[0-9]{5}$',
        'GA': r'^[0-9]{2}.*[0-9]{2}$',
        'GB': r'^[A-Z][A-Z0-9]{1,3}[0-9][A-Z]{2}$',
        'GE': r'^[0-9]{4}$',
        'GF': r'^[0-9]{5}$',
        'GG': r'^([A-Z]{2}[0-9]{2,3}[A-Z]{2})$',
        'GI': r'^GX111AA$',
        'GL': r'^[0-9]{4}$',
        'GP': r'^[0-9]{5}$',
        'GR': r'^[0-9]{5}$',
        'GS': r'^SIQQ1ZZ$',
        'GT': r'^[0-9]{5}$',
        'GU': r'^[0-9]{5}$',
        'GW': r'^[0-9]{4}$',
        'HM': r'^[0-9]{4}$',
        'HN': r'^[0-9]{5}$',
        'HR': r'^[0-9]{5}$',
        'HT': r'^[0-9]{4}$',
        'HU': r'^[0-9]{4}$',
        'ID': r'^[0-9]{5}$',
        'IL': r'^[0-9]{7}$',
        'IM': r'^IM[0-9]{2,3}[A-Z]{2}$$',
        'IN': r'^[0-9]{6}$',
        'IO': r'^[A-Z]{4}[0-9][A-Z]{2}$',
        'IQ': r'^[0-9]{5}$',
        'IR': r'^[0-9]{5}-[0-9]{5}$',
        'IS': r'^[0-9]{3}$',
        'IT': r'^[0-9]{5}$',
        'JE': r'^JE[0-9]{2}[A-Z]{2}$',
        'JM': r'^JM[A-Z]{3}[0-9]{2}$',
        'JO': r'^[0-9]{5}$',
        'JP': r'^[0-9]{3}-?[0-9]{4}$',
        'KE': r'^[0-9]{5}$',
        'KG': r'^[0-9]{6}$',
        'KH': r'^[0-9]{5}$',
        'KR': r'^[0-9]{3}-?[0-9]{3}$',
        'KY': r'^KY[0-9]-[0-9]{4}$',
        'KZ': r'^[0-9]{6}$',
        'LA': r'^[0-9]{5}$',
        'LB': r'^[0-9]{8}$',
        'LI': r'^[0-9]{4}$',
        'LK': r'^[0-9]{5}$',
        'LR': r'^[0-9]{4}$',
        'LS': r'^[0-9]{3}$',
        'LT': r'^(LT-)?[0-9]{5}$',
        'LU': r'^[0-9]{4}$',
        'LV': r'^LV-[0-9]{4}$',
        'LY': r'^[0-9]{5}$',
        'MA': r'^[0-9]{5}$',
        'MC': r'^980[0-9]{2}$',
        'MD': r'^MD-?[0-9]{4}$',
        'ME': r'^[0-9]{5}$',
        'MF': r'^[0-9]{5}$',
        'MG': r'^[0-9]{3}$',
        'MH': r'^[0-9]{5}$',
        'MK': r'^[0-9]{4}$',
        'MM': r'^[0-9]{5}$',
        'MN': r'^[0-9]{5}$',
        'MP': r'^[0-9]{5}$',
        'MQ': r'^[0-9]{5}$',
        'MT': r'^[A-Z]{3}[0-9]{4}$',
        'MV': r'^[0-9]{4,5}$',
        'MX': r'^[0-9]{5}$',
        'MY': r'^[0-9]{5}$',
        'MZ': r'^[0-9]{4}$',
        'NA': r'^[0-9]{5}$',
        'NC': r'^[0-9]{5}$',
        'NE': r'^[0-9]{4}$',
        'NF': r'^[0-9]{4}$',
        'NG': r'^[0-9]{6}$',
        'NI': r'^[0-9]{3}-[0-9]{3}-[0-9]$',
        'NL': r'^[0-9]{4}[A-Z]{2}$',
        'NO': r'^[0-9]{4}$',
        'NP': r'^[0-9]{5}$',
        'NZ': r'^[0-9]{4}$',
        'OM': r'^[0-9]{3}$',
        'PA': r'^[0-9]{6}$',
        'PE': r'^[0-9]{5}$',
        'PF': r'^[0-9]{5}$',
        'PG': r'^[0-9]{3}$',
        'PH': r'^[0-9]{4}$',
        'PK': r'^[0-9]{5}$',
        'PL': r'^[0-9]{2}-?[0-9]{3}$',
        'PM': r'^[0-9]{5}$',
        'PN': r'^[A-Z]{4}[0-9][A-Z]{2}$',
        'PR': r'^[0-9]{5}$',
        'PT': r'^[0-9]{4}(-?[0-9]{3})?$',
        'PW': r'^[0-9]{5}$',
        'PY': r'^[0-9]{4}$',
        'RE': r'^[0-9]{5}$',
        'RO': r'^[0-9]{6}$',
        'RS': r'^[0-9]{5}$',
        'RU': r'^[0-9]{6}$',
        'SA': r'^[0-9]{5}$',
        'SD': r'^[0-9]{5}$',
        'SE': r'^[0-9]{5}$',
        'SG': r'^([0-9]{2}|[0-9]{4}|[0-9]{6})$',
        'SH': r'^(STHL1ZZ|TDCU1ZZ)$',
        'SI': r'^(SI-)?[0-9]{4}$',
        'SK': r'^[0-9]{5}$',
        'SM': r'^[0-9]{5}$',
        'SN': r'^[0-9]{5}$',
        'SV': r'^01101$',
        'SZ': r'^[A-Z][0-9]{3}$',
        'TC': r'^TKCA1ZZ$',
        'TD': r'^[0-9]{5}$',
        'TH': r'^[0-9]{5}$',
        'TJ': r'^[0-9]{6}$',
        'TM': r'^[0-9]{6}$',
        'TN': r'^[0-9]{4}$',
        'TR': r'^[0-9]{5}$',
        'TT': r'^[0-9]{6}$',
        'TW': r'^[0-9]{5}$',
        'UA': r'^[0-9]{5}$',
        'US': r'^[0-9]{5}(-[0-9]{4}|-[0-9]{6})?$',
        'UY': r'^[0-9]{5}$',
        'UZ': r'^[0-9]{6}$',
        'VA': r'^00120$',
        'VC': r'^VC[0-9]{4}',
        'VE': r'^[0-9]{4}[A-Z]?$',
        'VG': r'^VG[0-9]{4}$',
        'VI': r'^[0-9]{5}$',
        'VN': r'^[0-9]{6}$',
        'WF': r'^[0-9]{5}$',
        'XK': r'^[0-9]{5}$',
        'YT': r'^[0-9]{5}$',
        'ZA': r'^[0-9]{4}$',
        'ZM': r'^[0-9]{5}$',
    }

    title = models.CharField(
        __(u"Treatment Pronouns for the contact", u"Title"),
        max_length=64, choices=TITLE_CHOICES, blank=True)

    # legal name
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

    email = models.EmailField("Email", max_length=200, blank=True)

    phone_number = models.CharField(
        max_length=100, blank=True,
        help_text='Enter your phone number. If it is a non-Indian number '
                  'please use the international format e.g.: +421 222 333 444')

    temple = models.CharField(
        max_length=100, blank=True,
        help_text=_('If person tells you association with temple, please enter '
                    'it here.')
    )

    # Following 5 fields are all part of the address
    address = models.TextField(
        _("Address"), max_length=255, blank=True)
    city = models.CharField(_("City"), max_length=255, blank=True)
    state = models.CharField(_("State/County"), max_length=255, blank=True)
    postcode = models.CharField(_("Post/Zip-code"), max_length=64, blank=True)
    country = CountryField()

    pan_card_number = models.CharField(
        _('PAN card number'), max_length=50, blank=True, null=True,
        validators=[
            RegexValidator(
                regex='[A-Za-z]{5}\d{4}[A-Za-z]{1}',
                message='Seems like invalid PAN Card Number.',
                code='invalid_pan_number'
            ),
        ],
        help_text=_('Required for Indian citizens. Enter your PAN card number.')
    )
    YATRA_CHOICES = (
        ('middle-east', _('Middle East')),
        ('north-america', _('North America')),
        ('russia', _('Russia')),
        ('south-africa', _('South Africa')),
        ('uk', _('UK')),
    )
    yatra = models.CharField(
        "Yatra", max_length=100, choices=YATRA_CHOICES, blank=True, null=True,
        help_text=_('If person belongs to one the of yatras in drowpdown, '
                    'please choose it'))

    location = models.CharField(_("Collection Location"), max_length=100,
                                blank=True)
    old_database_id = models.IntegerField(
        _('Old Database ID'), blank=True, null=True,
        help_text=_('If you are transfering data from old database (CiviCRM), '
                    'enter contact_id here. Otherwise leave empty.'))

    note = models.TextField(_("Note"), blank=True)

    def clean(self):
        # Strip all whitespace
        for field in ['first_name', 'middle_name', 'last_name',
                      'initiated_name', 'address', 'city',
                      'state', 'postcode', 'pan_card_number']:
            if self.__dict__[field]:
                self.__dict__[field] = self.__dict__[field].strip()

        # Ensure postcodes are valid for country
        self.ensure_postcode_is_valid_for_country()
        # Ensure either initiated name or legal name is entered
        self.ensure_name_is_entered()

    def ensure_name_is_entered(self):
        """
        Check that at least one of names is entered
        """
        if not ((self.first_name and self.last_name) or self.initiated_name):
            msg = _("Either initiated name of legal name has to be provided")
            raise exceptions.ValidationError({'initiated_name': [msg]})

    def ensure_postcode_is_valid_for_country(self):
        """
        Validate postcode given the country
        Source: django-oscar/src/oscar/apps/address/abstract_models.py
        """
        # if not self.postcode and self.country:
        #     regex = self.POSTCODES_REGEX.get(self.country.code, None)
        #     if regex:
        #         msg = _("Addresses in %(country)s require a valid postcode") \
        #             % {'country': self.country.name}
        #         raise exceptions.ValidationError({'postcode': msg})

        if self.postcode and self.country:
            # Ensure postcodes are always uppercase
            postcode = self.postcode.upper().replace(' ', '')
            regex = self.POSTCODES_REGEX.get(self.country.code, None)

            # Validate postcode against regex for the country if available
            if regex and not re.match(regex, postcode):
                msg = _("The postcode '%(postcode)s' is not valid "
                        "for %(country)s") \
                    % {'postcode': self.postcode,
                       'country': self.country.name}
                raise exceptions.ValidationError(
                    {'postcode': [msg]})

    def join_fields(self, fields, separator=u", "):
        """
        Join a sequence of fields using the specified separator
        """
        field_values = []
        for field in fields:
            # Title is special case
            if field == 'title':
                value = self.get_title_display()
            else:
                value = getattr(self, field)
            if value:
                field_values.append(value)
        return separator.join(filter(bool, field_values))

    def full_address(self, include_full_name=None):
        """
        Return the non-empty components of the address, but merging the
        title, first_name and last_name into a address field.
        """
        fields = [self.address, self.city, self.state, self.postcode,
                  self.country.name]
        if include_full_name:
            fields = [self.full_name] + fields
        fields = [f.strip() for f in fields if f]
        return fields

    @property
    def full_name(self):
        """
        Name (including title)
        """
        return self.join_fields(
            ('title', 'first_name', 'middle_name', 'last_name'),
            separator=u" ")

    @property
    def mixed_name(self):
        """
        Name (including title)
        """
        return self.join_fields(
            ('initiated_name', 'first_name', 'middle_name', 'last_name'),
            separator=u" ")

    @property
    def name(self):
        return self.join_fields(('first_name', 'middle_name', 'last_name'),
                                separator=u" ")

    @permalink
    def get_absolute_url(self):
        return ('contacts:person:detail', None, {'pk': self.pk})

    cache_contributions = None

    def get_contributions(self):
        """
        Returns all contributions of person
        """
        if not self.cache_contributions:
            from contributions.models import Contribution
            self.cache_contributions = Contribution.objects.all(). \
                filter(pledge__person=self)
        return self.cache_contributions

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
                        filter(pledge__person=self):
                    assigned_promotions.append(promotion)
            self.cache_assigned_promotions = assigned_promotions
        return self.cache_assigned_promotions

    has_ballance = None

    def get_has_ballance(self):
        if not self.cache_ballance:
            self.get_ballance()
        return self.has_ballance

    cache_ballance = None

    def get_ballance(self):
        """
        Calculates what person pledged to pay and what he already paid
        """
        # if we are calling this method in same request it will use cached
        # values instead of going through al pledges again
        if not self.cache_ballance:
            def get_financial_year(date):
                if date.month < 4:
                    year = date.year - 2001
                else:
                    year = date.year - 2000
                    return '%d-%d' % (year, year + 1)

            def ballance_dict():
                return {'pledged': 0,
                        'paid': 0,
                        'used': 0,
                        'available': 0,
                        'donated_total': 0,
                        'donated_year': 0,
                        'donated_financial_year': 0}

            ballance = {}
            for currency in settings.ENABLED_CURRENCIES:
                ballance[currency] = ballance_dict()

            today = datetime.datetime.now()
            current_financial_year = get_financial_year(today)

            Pledge = apps.get_model(app_label='contributions', model_name='Pledge')
            for pledge in Pledge.objects.all().filter(person=self):
                ballance[pledge.currency]['pledged'] += pledge.amount
                ballance[pledge.currency]['paid'] += pledge.amount_paid or 0
                self.has_ballance = True

                for contribution in pledge.contributions.all():
                    if contribution.status == 'completed':
                        if today.year == contribution.cleared_on.year:
                            ballance[pledge.currency]['donated_year'] += contribution.amount
                        if contribution.generate_serial_year() == current_financial_year:
                            ballance[pledge.currency]['donated_financial_year'] += contribution.amount

            for promotion in self.assigned_promotions():
                currency = promotion.pledge.currency
                if hasattr(promotion, 'quantity'):
                    ballance[currency]['used'] += \
                        promotion.quantity * promotion.amount[currency]
                else:
                    ballance[currency]['used'] += promotion.amount[currency]

            # calculate unused ballance for each currency
            for currency in ballance:
                ballance[currency]['available'] = \
                    ballance[currency]['pledged'] - ballance[currency]['used']
            self.cache_ballance = ballance
        return self.cache_ballance

    def __str__(self):
        return self.mixed_name

    class Meta:
        permissions = (("can_export", "Can export"),)
