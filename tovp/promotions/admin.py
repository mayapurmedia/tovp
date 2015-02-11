from django.contrib import admin
from reversion_compare.admin import CompareVersionAdmin

from .models import (NrsimhaTile, GoldenBrick, RadhaMadhavaBrick,
                     SilverCoin, GoldCoin, PlatinumCoin,
                     SquareFeet, SquareMeter, Trustee)


class NrsimhaTileModelAdmin(CompareVersionAdmin):
    class Meta:
        model = NrsimhaTile


class GoldenBrickModelAdmin(CompareVersionAdmin):
    class Meta:
        model = GoldenBrick


class RadhaMadhavaBrickModelAdmin(CompareVersionAdmin):
    class Meta:
        model = RadhaMadhavaBrick


class SilverCoinModelAdmin(CompareVersionAdmin):
    class Meta:
        model = SilverCoin


class GoldCoinModelAdmin(CompareVersionAdmin):
    class Meta:
        model = GoldCoin


class PlatinumCoinModelAdmin(CompareVersionAdmin):
    class Meta:
        model = PlatinumCoin


class SquareFeetModelAdmin(CompareVersionAdmin):
    class Meta:
        model = SquareFeet


class SquareMeterModelAdmin(CompareVersionAdmin):
    class Meta:
        model = SquareMeter


class TrusteeModelAdmin(CompareVersionAdmin):
    class Meta:
        model = Trustee


admin.site.register(NrsimhaTile, NrsimhaTileModelAdmin)
admin.site.register(GoldenBrick, GoldenBrickModelAdmin)
admin.site.register(RadhaMadhavaBrick, RadhaMadhavaBrickModelAdmin)
admin.site.register(SilverCoin, SilverCoinModelAdmin)
admin.site.register(GoldCoin, GoldCoinModelAdmin)
admin.site.register(PlatinumCoin, PlatinumCoinModelAdmin)
admin.site.register(SquareFeet, SquareFeetModelAdmin)
admin.site.register(SquareMeter, SquareMeterModelAdmin)
admin.site.register(Trustee, TrusteeModelAdmin)
