from django.apps import apps
from django.views.generic.base import TemplateView
from collections import OrderedDict

from promotions import models


ENABLED_PROMOTIONS = OrderedDict(
    [
        # ('nrsimha-tile', apps.get_model("promotions", "NrsimhaTile")),
        # ('golden-brick', apps.get_model("promotions", "GoldenBrick")),
        # ('radha-madhava-brick', apps.get_model("promotions", "RadhaMadhavaBrick")),
        # ('general-donation', apps.get_model("promotions", "GeneralDonation")),
    ]
)
#
#
# ENABLED_PROMOTIONS = {
#     'nrsimha_tile': apps.get_model("promotions", "NrsimhaTile"),
#     'golden_brick': apps.get_model("promotions", "GoldenBrick"),
#     'general_donation': apps.get_model("promotions", "GeneralDonation"),
# }

class SelectRegionView(TemplateView):
    template_name = "donate/select_region.html"

    def get_context_data(self, **kwargs):
        context = super(SelectRegionView, self).get_context_data(**kwargs)
        context['promotion'] = ENABLED_PROMOTIONS[kwargs['promotion_slug']]
        return context


class DonateView(TemplateView):
    template_name = "donate/donate.html"

    def get_context_data(self, **kwargs):
        context = super(DonateView, self).get_context_data(**kwargs)
        context['promotions'] = [ENABLED_PROMOTIONS[item] for item in ENABLED_PROMOTIONS]
        return context


class BaseDonatePromotionView(TemplateView):
    template_name = "donate/donate_nrsimha.html"
    REGION_TO_CURRENCY = {
        'international': {
            'code': 'USD',
            'sign': '$'
        },
        'india': {
            'code': 'INR',
            'sign': '₹',
        },
        'uk': {
            'code': 'GBP',
            'sign': '£',
        },
    }

    def get_context_data(self, **kwargs):
        context = super(BaseDonatePromotionView, self).get_context_data(**kwargs)
        currency = self.REGION_TO_CURRENCY[kwargs['region']]
        context['promotion'] = self.model
        context['amount_grid'] = self.model.amount_grid[currency['code']]
        context['region'] = kwargs['region']
        context['currency'] = currency
        return context


class DonateNrsimhaTileView(BaseDonatePromotionView):
    template_name = "donate/donate_nrsimha.html"
    model = models.NrsimhaTile


class DonateGoldenBrickView(BaseDonatePromotionView):
    # template_name = "donate/donate_golden_brick.html"
    template_name = "donate/donate_nrsimha.html"
    model = models.GoldenBrick

class DonateGeneralView(BaseDonatePromotionView):
    # template_name = "donate/donate_general.html"
    template_name = "donate/donate_nrsimha.html"
    model = models.GeneralDonation

class DonateRadhaMadhavaBrickView(BaseDonatePromotionView):
    template_name = "donate/donate_nrsimha.html"
    model = models.RadhaMadhavaBrick

