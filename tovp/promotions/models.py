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
        promotion_slug = cls._meta.verbose_name.replace(' ', '_')
        return reverse('promotions:%s:create' % promotion_slug, None,
                       kwargs={'person_id': person_id, 'pledge_id': pledge_id})

    def get_absolute_url(self):
        promotion_slug = self._meta.verbose_name.replace(' ', '_')
        return reverse('promotions:%s:detail' % promotion_slug, None,
                       kwargs={'person_id': self.pledge.person.pk,
                               'pledge_id': self.pledge.pk,
                               'pk': self.pk})

    def get_update_url(self):
        promotion_slug = self._meta.verbose_name.replace(' ', '_')
        return reverse('promotions:%s:update' % promotion_slug, None,
                       kwargs={'person_id': self.pledge.person.pk,
                               'pledge_id': self.pledge.pk,
                               'pk': self.pk})

    def get_delete_url(self):
        promotion_slug = self._meta.verbose_name.replace(' ', '_')
        return reverse('promotions:%s:delete' % promotion_slug, None,
                       kwargs={'person_id': self.pledge.person.pk,
                               'pledge_id': self.pledge.pk,
                               'pk': self.pk})

    def __str__(self):
        return '{promotion_title}'.format(
            promotion_title=self._meta.verbose_name.title())

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
        ('need_to_send', _('Need to send to DC')),
        ('name_given', _('Name given to DC')),
        ('brick_made', _('Brick is made')),
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
        'USD': 1000,
        'EUR': 1000,
        'GBP': 800,
    }


class GoldenBrick(BaseBrick):
    amount = {
        'INR': 100000,
        'USD': 1600,
        'EUR': 1500,
        'GBP': 1300,
    }


class GuruParamparaBrick(BaseBrick):
    amount = {
        'INR': 100000,
        'USD': 1600,
        'EUR': 1500,
        'GBP': 1300,
    }


class RadhaMadhavaBrick(BaseBrick):
    amount = {
        'INR': 150000,
        'USD': 2500,
        'EUR': 2400,
        'GBP': 2200,
    }


class SilverCoin(BaseCoin):
    amount = {
        'INR': 650000,
        'USD': 11000,
        'EUR': 10000,
        'GBP': 9000,
    }


class GoldCoin(BaseCoin):
    amount = {
        'INR': 6500000,
        'USD': 108000,
        'EUR': 108000,
        'GBP': 108000,
    }


class PlatinumCoin(BaseCoin):
    amount = {
        'INR': 15000000,
        'USD': 250000,
        'EUR': 240000,
        'GBP': 220000,
    }


class SquareFeet(CertificateGivenMixin, BasePromotion):
    amount = {
        'INR': 7000,
        'USD': 150,
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
        'USD': 1500,
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
        'USD': 1000000,
        'EUR': 1000000,
        'GBP': 850000,
    }


class GeneralDonation(BasePromotion):
    amount = {
        'INR': 1,
        'USD': 1,
        'EUR': 1,
        'GBP': 1,
    }


promotions = [NrsimhaTile, GoldenBrick, GuruParamparaBrick, RadhaMadhavaBrick,
              SilverCoin, GoldCoin, PlatinumCoin,
              SquareFeet, SquareMeter, Trustee, GeneralDonation]
