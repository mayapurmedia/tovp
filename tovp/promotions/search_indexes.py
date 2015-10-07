from haystack import indexes

from ananta.search_indexes import ContentSearchIndexMixin
from contacts.search_indexes import PledgePersonSearchIndexMixin

from .models import (NrsimhaTile, GoldenBrick, GuruParamparaBrick,
                     RadhaMadhavaBrick, SilverCoin, GadadharCoin, AdvaitaCoin,
                     GoldCoin, PlatinumCoin, RadharaniCoin,
                     SquareFeet, SquareMeter, Trustee, GeneralDonation)


class PromotionIndexMixin(ContentSearchIndexMixin, PledgePersonSearchIndexMixin,
                          indexes.SearchIndex):
    content_name = 'Promotion'
    promotion_type = indexes.CharField(faceted=True)
    text = indexes.CharField(
        document=True, use_template=True,
        template_name='search/indexes/promotions/brick_text.txt')

    status = indexes.CharField(model_attr='pledge__get_status_display', faceted=True)
    absolute_url = indexes.CharField(model_attr='pledge__person__get_absolute_url')
    source = indexes.MultiValueField(null=True, faceted=True)

    def get_model(self):
        try:
            return self.model
        except:
            pass

    def prepare_source(self, obj):
        items = []
        if getattr(obj, 'pledge', None) and obj.pledge.source:
            source = obj.pledge.get_source_display()
            if source not in items:
                items.append(source)
                if obj.pledge.source in ['jps-office', 'namahatta',
                                         'jps-others']:
                    items.append('JPS (All combined)')
        return items

    def prepare_promotion_type(self, obj):
        try:
            return self.get_model()._meta.verbose_name.title()
            # return self.promotion_type
        except:
            return 'Noname'


class BrickIndex(PromotionIndexMixin):
    name_on_brick = indexes.CharField(model_attr='name_on_brick')
    coin_given = indexes.CharField(faceted=True)
    certificate_given = indexes.CharField(faceted=True)

    def prepare_coin_given(self, obj):
        if not obj.coin_given:
            return 'No'
        return 'Yes'

    def prepare_certificate_given(self, obj):
        if not obj.certificate_given:
            return 'No'
        return 'Yes'


class NrsimhaTileIndex(BrickIndex, indexes.Indexable):
    model = NrsimhaTile


class GoldenBrickIndex(BrickIndex, indexes.Indexable):
    model = GoldenBrick


class GuruParamparaBrickIndex(BrickIndex, indexes.Indexable):
    model = GuruParamparaBrick


class RadhaMadhavaBrickIndex(BrickIndex, indexes.Indexable):
    model = RadhaMadhavaBrick


class CoinIndex(PromotionIndexMixin):
    coin_given = indexes.CharField(faceted=True)
    certificate_given = indexes.CharField(faceted=True)

    def prepare_coin_given(self, obj):
        if not obj.coin_given:
            return 'No'
        return 'Yes'

    def prepare_certificate_given(self, obj):
        if not obj.certificate_given:
            return 'No'
        return 'Yes'


class SilverCoinIndex(PromotionIndexMixin, indexes.Indexable):
    model = SilverCoin


class GadadharCoinIndex(PromotionIndexMixin, indexes.Indexable):
    model = GadadharCoin


class AdvaitaCoinIndex(PromotionIndexMixin, indexes.Indexable):
    model = AdvaitaCoin


class GoldCoinIndex(PromotionIndexMixin, indexes.Indexable):
    model = GoldCoin


class PlatinumCoinIndex(PromotionIndexMixin, indexes.Indexable):
    model = PlatinumCoin


class RadharaniCoinIndex(PromotionIndexMixin, indexes.Indexable):
    model = RadharaniCoin


class SquareFeetIndex(PromotionIndexMixin, indexes.Indexable):
    model = SquareFeet
    quantity = indexes.IntegerField(model_attr='quantity')


class SquareMeterIndex(PromotionIndexMixin, indexes.Indexable):
    model = SquareMeter
    quantity = indexes.IntegerField(model_attr='quantity')


class TrusteeIndex(PromotionIndexMixin, indexes.Indexable):
    model = Trustee


class GeneralDonationIndex(PromotionIndexMixin, indexes.Indexable):
    model = GeneralDonation
