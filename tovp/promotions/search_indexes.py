from haystack import indexes

from ananta.search_indexes import ContentSearchIndexMixin
from contacts.search_indexes import PledgePersonSearchIndexMixin

from .models import (NrsimhaTile, GoldenBrick, GuruParamparaBrick,
                     RadhaMadhavaBrick, SilverCoin, GoldCoin, PlatinumCoin,
                     SquareFeet, SquareMeter, Trustee)


class PromotionIndexMixin(ContentSearchIndexMixin, PledgePersonSearchIndexMixin,
                          indexes.SearchIndex):
    content_name = 'Promotion'
    promotion_type = indexes.CharField(faceted=True)
    text = indexes.CharField(
        document=True, use_template=True,
        template_name='search/indexes/promotions/brick_text.txt')

    status = indexes.CharField(model_attr='pledge__get_status_display', faceted=True)
    absolute_url = indexes.CharField(model_attr='pledge__person__get_absolute_url')

    def get_model(self):
        try:
            return self.model
        except:
            pass

    def prepare_promotion_type(self, obj):
        try:
            return self.get_model()._meta.verbose_name.title()
            # return self.promotion_type
        except:
            return 'Noname'


class BrickIndex(PromotionIndexMixin):
    name_on_brick = indexes.CharField(model_attr='name_on_brick')


class NrsimhaTileIndex(BrickIndex, indexes.Indexable):
    model = NrsimhaTile


class GoldenBrickIndex(BrickIndex, indexes.Indexable):
    model = GoldenBrick


class GuruParamparaBrickIndex(BrickIndex, indexes.Indexable):
    model = GuruParamparaBrick


class RadhaMadhavaBrickIndex(BrickIndex, indexes.Indexable):
    model = RadhaMadhavaBrick


class CoinIndex(PromotionIndexMixin):
    pass


class SilverCoinIndex(PromotionIndexMixin, indexes.Indexable):
    model = SilverCoin


class GoldCoinIndex(PromotionIndexMixin, indexes.Indexable):
    model = GoldCoin


class PlatinumCoinIndex(PromotionIndexMixin, indexes.Indexable):
    model = PlatinumCoin


class SquareFeetIndex(PromotionIndexMixin, indexes.Indexable):
    model = SquareFeet
    quantity = indexes.IntegerField(model_attr='quantity')


class SquareMeterIndex(PromotionIndexMixin, indexes.Indexable):
    model = SquareMeter
    quantity = indexes.IntegerField(model_attr='quantity')


class TrusteeIndex(PromotionIndexMixin, indexes.Indexable):
    model = Trustee
