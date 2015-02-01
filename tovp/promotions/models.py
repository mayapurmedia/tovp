from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from model_utils.models import TimeStampedModel

from contributions.models import Pledge


class BasePromotion(TimeStampedModel):
    pledge = models.ForeignKey(Pledge, verbose_name="Pledge",  # blank=True,
                               related_name='+')

    @classmethod
    def get_amount(cls, currency):
        functions = {
            'INR': cls.amount_rs,
            'USD': cls.amount_usd,
        }
        return functions[currency]

    @classmethod
    def is_eligible(cls, person_ballance):
        if cls.amount_rs <= person_ballance['INR']['available']:
            return True
        if cls.amount_usd <= person_ballance['USD']['available']:
            return True
        return None

    class Meta:
        abstract = True


class BaseBrick(BasePromotion):
    name_on_brick = models.TextField(
        _("Name on the brick"), max_length=100, blank=True,
        help_text=_("Enter name which will be on the brick. Maximum 100 "
                    "characters."))

    def __str__(self):
        return '{brick_title} ({name})'.format(
            brick_title=self._meta.verbose_name.title(),
            name=self.name_on_brick or '*None*')

    class Meta:
        abstract = True


class BaseCoin(BasePromotion):
    class Meta:
        abstract = True


class NrsimhaTile(BaseBrick):
    amount_rs = 51000
    amount_usd = 1000

    @classmethod
    def get_create_url(cls, person_id):
        return reverse('promotions:nrsimha_tile:create', None,
                       kwargs={'person_id': person_id})


class GoldenBrick(BaseBrick):
    amount_rs = 100000
    amount_usd = 1600

    @classmethod
    def get_create_url(cls, person_id):
        return reverse('promotions:golden_brick:create', None,
                       kwargs={'person_id': person_id})


class RadhaMadhavaBrick(BaseBrick):
    amount_rs = 150000
    amount_usd = 2500

    @classmethod
    def get_create_url(cls, person_id):
        return reverse('promotions:radha_madhava_brick:create', None,
                       kwargs={'person_id': person_id})


class SilverCoin(BaseCoin):
    amount_rs = 650000
    amount_usd = 11000

    @classmethod
    def get_create_url(cls, person_id):
        return reverse('promotions:silver_coin:create', None,
                       kwargs={'person_id': person_id})


class GoldCoin(BaseCoin):
    amount_rs = 6500000
    amount_usd = 108000

    @classmethod
    def get_create_url(cls, person_id):
        return reverse('promotions:gold_coin:create', None,
                       kwargs={'person_id': person_id})


class PlatinumCoin(BaseCoin):
    amount_rs = 15000000
    amount_usd = 250000

    @classmethod
    def get_create_url(cls, person_id):
        return reverse('promotions:platinum_coin:create', None,
                       kwargs={'person_id': person_id})


class SquareFeet(BasePromotion):
    amount_rs = 7000
    amount_usd = 150

    @classmethod
    def get_create_url(cls, person_id):
        return reverse('promotions:square_feet:create', None,
                       kwargs={'person_id': person_id})


class SquareMeter(BasePromotion):
    amount_rs = 70000
    amount_usd = 1500

    @classmethod
    def get_create_url(cls, person_id):
        return reverse('promotions:square_meter:create', None,
                       kwargs={'person_id': person_id})


class Trustee(BasePromotion):
    amount_rs = 51000000
    amount_usd = 1000000

    @classmethod
    def get_create_url(cls, person_id):
        return reverse('promotions:trustee:create', None,
                       kwargs={'person_id': person_id})


promotions = [NrsimhaTile, GoldenBrick, RadhaMadhavaBrick,
              SilverCoin, GoldCoin, PlatinumCoin,
              SquareFeet, SquareMeter, Trustee]
