from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from model_utils.models import TimeStampedModel, MonitorField
from audit_log.models import AuthStampedModel

from contributions.models import Pledge


class BasePromotion(AuthStampedModel, TimeStampedModel):
    pledge = models.ForeignKey(Pledge, verbose_name="Pledge",  # blank=True,
                               related_name='+')

    @classmethod
    def get_amount(cls, currency):
        return cls.amount[currency]

    @classmethod
    def is_eligible(cls, person_ballance):
        for currency in cls.amount:
            if cls.amount[currency] <= person_ballance[currency]['available']:
                return True
        return None

    @classmethod
    def get_create_url(cls, person_id, pledge_id):
        promotion_slug = cls.get_promotion_slug()
        return reverse('promotions:%s:create' % promotion_slug, None,
                       kwargs={'person_id': person_id, 'pledge_id': pledge_id})

    @classmethod
    def get_promotion_slug(cls):
        return cls._meta.verbose_name.replace(' ', '-').lower()

    @classmethod
    def get_donate_url(cls, region):
        promotion_slug = cls.get_promotion_slug()
        return reverse('donate:%s' % promotion_slug, args=[region])

    def get_absolute_url(self):
        promotion_slug = self.get_promotion_slug()
        return reverse('promotions:%s:detail' % promotion_slug, None,
                       kwargs={'person_id': self.pledge.person.pk,
                               'pledge_id': self.pledge.pk,
                               'pk': self.pk})

    def get_update_url(self):
        promotion_slug = self.get_promotion_slug()
        return reverse('promotions:%s:update' % promotion_slug, None,
                       kwargs={'person_id': self.pledge.person.pk,
                               'pledge_id': self.pledge.pk,
                               'pk': self.pk})

    def get_delete_url(self):
        promotion_slug = self.get_promotion_slug()
        return reverse('promotions:%s:delete' % promotion_slug, None,
                       kwargs={'person_id': self.pledge.person.pk,
                               'pledge_id': self.pledge.pk,
                               'pk': self.pk})

    def __str__(self):
        return '{promotion_title}'.format(
            promotion_title=self._meta.verbose_name.title())

    def meta(self):
        return self._meta

    class Meta:
        abstract = True


class CertificateGivenMixin(models.Model):
    certificate_given = models.BooleanField(
        default=False, db_index=True,
        help_text='Has certificate for this promotion been given?')
    certificate_given_date = MonitorField(monitor='certificate_given')

    class Meta:
        abstract = True


class CoinGivenMixin(models.Model):
    coin_given = models.BooleanField(
        default=False, db_index=True,
        help_text='Has coin for this promotion been given?')
    coin_given_date = MonitorField(monitor='coin_given')

    class Meta:
        abstract = True


class BaseBrick(CertificateGivenMixin, CoinGivenMixin, BasePromotion):
    name_on_brick = models.TextField(
        _("Name on the brick"), max_length=100, blank=True,
        help_text=_("Enter name which will be on the brick. Maximum 36 "
                    "characters."))

    BRICK_STATUS_CHOICES = (
        ('need_to_send', _('Need to produce')),
        ('name_given', _('In production')),
        ('brick_made', _('Finished')),
    )
    brick_status = models.CharField("Brick Status", max_length=100,
                                    default='need_to_send',
                                    choices=BRICK_STATUS_CHOICES)

    def __str__(self):
        return '{promotion_title} ({name}) — Coin={coin}, Cert={certificate}'. \
            format(
                promotion_title=self._meta.verbose_name.title(),
                name=self.name_on_brick or '*None*',
                coin='Yes' if self.coin_given else 'No',
                certificate='Yes' if self.certificate_given else 'No')

    class Meta:
        abstract = True


class BaseCoin(CertificateGivenMixin, CoinGivenMixin, BasePromotion):
    class Meta:
        abstract = True

    def __str__(self):
        return '{promotion_title} — Coin={coin}, Cert={certificate}'.format(
            promotion_title=self._meta.verbose_name.title(),
            coin='Yes' if self.coin_given else 'No',
            certificate='Yes' if self.certificate_given else 'No')


class NrsimhaTile(BaseBrick):
    amount = {
        'INR': 51000,
        'RUB': 30000,
        'USD': 1000,
        'CAD': 1000,
        'EUR': 1000,
        'GBP': 800,
    }
    amount_grid = {
        'INR': (
            {'months': 1, 'amount': 51000, 'default': True},
            {'months': 2, 'amount': 25500},
            {'months': 5, 'amount': 10200},
            {'months': 12, 'amount': 4300},
            {'months': 24, 'amount': 2150},
        ),
        'USD': (
            {'months': 1, 'amount': 1000, 'default': True},
            {'months': 2, 'amount': 500},
            {'months': 5, 'amount': 200},
            {'months': 12, 'amount': 84},
            {'months': 24, 'amount': 42},
        ),
        'GBP': (
            {'months': 1, 'amount': 800, 'default': True},
            {'months': 2, 'amount': 400},
            {'months': 5, 'amount': 160},
            {'months': 12, 'amount': 70},
            {'months': 24, 'amount': 35},
        ),
    }

    class Meta:
        verbose_name = 'Nrsimha Tile'


class GoldenBrick(BaseBrick):
    amount = {
        'INR': 100000,
        'RUB': 50000,
        'USD': 1600,
        'CAD': 1600,
        'EUR': 1500,
        'GBP': 1300,
    }
    amount_grid = {
        'INR': (
            {'months': 1, 'amount': 100000, 'default': True},
            {'months': 2, 'amount': 50000},
            {'months': 5, 'amount': 20000},
            {'months': 12, 'amount': 8500},
            {'months': 24, 'amount': 4750},
        ),
        'USD': (
            {'months': 1, 'amount': 1600, 'default': True},
            {'months': 2, 'amount': 800},
            {'months': 5, 'amount': 320},
            {'months': 12, 'amount': 140},
            {'months': 24, 'amount': 70},
        ),
        'GBP': (
            {'months': 1, 'amount': 1300, 'default': True},
            {'months': 2, 'amount': 400},
            {'months': 5, 'amount': 260},
            {'months': 12, 'amount': 110},
            {'months': 24, 'amount': 55},
        ),
    }

    class Meta:
        verbose_name = 'Golden Brick'

class GuruParamparaBrick(BaseBrick):
    amount = {
        'INR': 100000,
        'RUB': 50000,
        'USD': 1600,
        'CAD': 1600,
        'EUR': 1500,
        'GBP': 1300,
    }


class RadhaMadhavaBrick(BaseBrick):
    amount = {
        'INR': 150000,
        'RUB': 100000,
        'USD': 2500,
        'CAD': 2500,
        'EUR': 2400,
        'GBP': 2200,
    }
    amount_grid = {
        'INR': (
            {'months': 1, 'amount': 150000, 'default': True},
            {'months': 2, 'amount': 75000},
            {'months': 5, 'amount': 30000},
            {'months': 12, 'amount': 12500},
            {'months': 24, 'amount': 6750},
        ),
        'USD': (
            {'months': 1, 'amount': 2500, 'default': True},
            {'months': 2, 'amount': 1250},
            {'months': 5, 'amount': 500},
            {'months': 12, 'amount': 210},
            {'months': 24, 'amount': 108},
            {'months': 50, 'amount': 50},
        ),
        'GBP': (
            {'months': 1, 'amount': 2200, 'default': True},
            {'months': 2, 'amount': 1100},
            {'months': 5, 'amount': 440},
            {'months': 12, 'amount': 190},
            {'months': 24, 'amount': 95},
        ),
    }

    class Meta:
        verbose_name = 'Radha Madhava Brick'

class SilverCoin(BaseCoin):
    amount = {
        'INR': 650000,
        'RUB': 500000,
        'USD': 11000,
        'CAD': 11000,
        'EUR': 10000,
        'GBP': 9000,
    }

    class Meta:
        verbose_name = 'Srivas Coin'


class GadadharCoin(BaseCoin):
    amount = {
        'INR': 1500000,
        'RUB': 1500000,
        'USD': 25000,
        'CAD': 25000,
        'EUR': 25000,
        'GBP': 25000,
    }

    class Meta:
        verbose_name = 'Gadadhar Coin'


class AdvaitaCoin(BaseCoin):
    amount = {
        'INR': 3100000,
        'RUB': 3100000,
        'USD': 51000,
        'CAD': 51000,
        'EUR': 51000,
        'GBP': 51000,
    }

    class Meta:
        verbose_name = 'Advaita Coin'


class GoldCoin(BaseCoin):
    amount = {
        'INR': 6500000,
        'RUB': 5000000,
        'USD': 108000,
        'CAD': 108000,
        'EUR': 108000,
        'GBP': 108000,
    }

    class Meta:
        verbose_name = 'Nityananda Coin'


class PlatinumCoin(BaseCoin):
    amount = {
        'INR': 15000000,
        'RUB': 11000000,
        'USD': 250000,
        'CAD': 250000,
        'EUR': 240000,
        'GBP': 220000,
    }

    class Meta:
        verbose_name = 'Caitanya Coin'


class RadharaniCoin(BaseCoin):
    amount = {
        'INR': 60000000,
        'RUB': 60000000,
        'USD': 1000000,
        'CAD': 1000000,
        'EUR': 1000000,
        'GBP': 1000000,
    }

    class Meta:
        verbose_name = 'Radharani Coin'


class SquareFeet(CertificateGivenMixin, BasePromotion):
    amount = {
        'INR': 7000,
        'RUB': 5000,
        'USD': 150,
        'CAD': 150,
        'EUR': 140,
        'GBP': 130,
    }

    quantity = models.PositiveIntegerField(
        _('Quantity'), default=1,
        help_text=_("Enter how many feets you want to add."))

    def __str__(self):
        return '{quantity}x {promotion_title} — Cert={certificate}'.format(
            quantity=self.quantity,
            promotion_title=self._meta.verbose_name.title(),
            certificate='Yes' if self.certificate_given else 'No')


class SquareMeter(CertificateGivenMixin, BasePromotion):
    amount = {
        'INR': 70000,
        'RUB': 50000,
        'USD': 1500,
        'CAD': 1500,
        'EUR': 1400,
        'GBP': 1300,
    }

    quantity = models.PositiveIntegerField(
        _('Quantity'), default=1,
        help_text=_("Enter how many meters you want to add."))

    def __str__(self):
        return '{quantity}x {promotion_title} — Cert={certificate}'.format(
            quantity=self.quantity,
            promotion_title=self._meta.verbose_name.title(),
            certificate='Yes' if self.certificate_given else 'No')


class Trustee(BasePromotion):
    amount = {
        'INR': 51000000,
        'RUB': 51000000,
        'USD': 1000000,
        'CAD': 1000000,
        'EUR': 1000000,
        'GBP': 850000,
    }


class GeneralDonation(BasePromotion):
    amount = {
        'INR': 1,
        'RUB': 1,
        'USD': 1,
        'CAD': 1,
        'EUR': 1,
        'GBP': 1,
    }
    amount_grid = {
        'INR': (
            {'months': 1, 'amount': 100000, 'default': True},
            {'months': 2, 'amount': 200000},
            {'months': 5, 'amount': 20000},
            {'months': 12, 'amount': 8500},
            {'months': 24, 'amount': 4750},
        ),
        'USD': (
            {'months': 1, 'amount': 1600, 'default': True},
            {'months': 2, 'amount': 800},
            {'months': 5, 'amount': 320},
            {'months': 12, 'amount': 140},
            {'months': 24, 'amount': 70},
        ),
        'GBP': (
            {'months': 1, 'amount': 1300, 'default': True},
            {'months': 2, 'amount': 400},
            {'months': 5, 'amount': 260},
            {'months': 12, 'amount': 110},
            {'months': 24, 'amount': 55},
        ),
    }

    class Meta:
        verbose_name = 'General Donation'


promotions = [NrsimhaTile, GoldenBrick, GuruParamparaBrick, RadhaMadhavaBrick,
              SilverCoin, GadadharCoin, AdvaitaCoin, GoldCoin, PlatinumCoin,
              RadharaniCoin, SquareFeet, SquareMeter, Trustee, GeneralDonation]
