from django import forms

from contributions.models import Pledge

from .models import (NrsimhaTile, GoldenBrick, GuruParamparaBrick,
                     RadhaMadhavaBrick, SilverCoin, GoldCoin, PlatinumCoin,
                     SquareFeet, SquareMeter, Trustee, GeneralDonation)


class PromotionForm(forms.ModelForm):
    def __init__(self, person, *args, **kwargs):
        super(PromotionForm, self).__init__(*args, **kwargs)
        self.fields['pledge'].queryset = Pledge.objects.filter(
            person=person)


class BaseBrickForm(PromotionForm):
    class Meta():
        exclude = ('status_changed', 'certificate_given_date',
                   'coin_given_date')
        widgets = {
            'name_on_brick': forms.Textarea(attrs={'rows': 2}),
        }


class NrsimhaTileForm(BaseBrickForm):
    class Meta(BaseBrickForm.Meta):
        model = NrsimhaTile


class GoldenBrickForm(BaseBrickForm):
    class Meta(BaseBrickForm.Meta):
        model = GoldenBrick


class GuruParamparaBrickForm(BaseBrickForm):
    class Meta(BaseBrickForm.Meta):
        model = GuruParamparaBrick


class RadhaMadhavaBrickForm(BaseBrickForm):
    class Meta(BaseBrickForm.Meta):
        model = RadhaMadhavaBrick


class BaseCoinForm(PromotionForm):
    class Meta:
        exclude = ['certificate_given_date', 'coin_given_date']


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
        exclude = ['certificate_given_date']


class SquareMeterForm(BaseGeneralPromotionForm):
    class Meta(BaseCoinForm.Meta):
        model = SquareMeter
        exclude = ['certificate_given_date']


class TrusteeForm(BaseGeneralPromotionForm):
    class Meta(BaseCoinForm.Meta):
        model = Trustee


class GeneralDonationForm(BaseGeneralPromotionForm):
    class Meta(BaseCoinForm.Meta):
        model = GeneralDonation
