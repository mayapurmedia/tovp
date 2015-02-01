from django import forms

from contributions.models import Pledge

from .models import (NrsimhaTile, GoldenBrick, RadhaMadhavaBrick,
                     SilverCoin, GoldCoin, PlatinumCoin,
                     SquareFeet, SquareMeter, Trustee)


class PromotionForm(forms.ModelForm):
    def __init__(self, person, *args, **kwargs):
        super(PromotionForm, self).__init__(*args, **kwargs)
        self.fields['pledge'].queryset = Pledge.objects.filter(
            person=person)


class BaseBrickForm(PromotionForm):
    class Meta():
        exclude = ('status_changed',)
        widgets = {
            'name_on_brick': forms.Textarea(attrs={'rows': 2}),
        }


class NrsimhaTileForm(BaseBrickForm):
    class Meta(BaseBrickForm.Meta):
        model = NrsimhaTile


class GoldenBrickForm(BaseBrickForm):
    class Meta(BaseBrickForm.Meta):
        model = GoldenBrick


class RadhaMadhavaBrickForm(BaseBrickForm):
    class Meta(BaseBrickForm.Meta):
        model = RadhaMadhavaBrick


class BaseCoinForm(PromotionForm):
    class Meta:
        exclude = []


class SilverCoinForm(BaseCoinForm):
    class Meta(BaseCoinForm.Meta):
        model = SilverCoin


class GoldCoinForm(BaseCoinForm):
    class Meta(BaseCoinForm.Meta):
        model = GoldCoin


class PlatinumCoinForm(BaseCoinForm):
    class Meta(BaseCoinForm.Meta):
        model = PlatinumCoin


class BaseGeneralPromotionForm(PromotionForm):
    class Meta:
        exclude = []


class SquareFeetForm(BaseGeneralPromotionForm):
    class Meta(BaseCoinForm.Meta):
        model = SquareFeet


class SquareMeterForm(BaseGeneralPromotionForm):
    class Meta(BaseCoinForm.Meta):
        model = SquareMeter


class TrusteeForm(BaseGeneralPromotionForm):
    class Meta(BaseCoinForm.Meta):
        model = Trustee