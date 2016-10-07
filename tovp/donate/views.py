from django.apps import apps
from django.views.generic.base import TemplateView
from django.urls import reverse


class DonateView(TemplateView):
    template_name = "donate/donate.html"

    def get_context_data(self, **kwargs):
        context = super(DonateView, self).get_context_data(**kwargs)
        context['promotions'] = [
            # apps.get_model("promotions", "NrsimhaTile"),
            # apps.get_model("promotions", "GoldenBrick"),
            # apps.get_model("promotions", "RadhaMadhavaBrick"),
            # apps.get_model("promotions", "SilverCoin"),
            # apps.get_model("promotions", "GadadharCoin"),
            # apps.get_model("promotions", "AdvaitaCoin"),
            # apps.get_model("promotions", "SquareFeet"),
            # apps.get_model("promotions", "GeneralDonation"),
            # GuruParamparaBrick, GoldCoin, PlatinumCoin, RadharaniCoin,
            # SquareMeter, Trustee
        ]
        return context


class DonateNrsimhaTileView(TemplateView):
    template_name = "donate/donate_nrsimha.html"

class DonateGoldenBrickView(TemplateView):
    template_name = "donate/donate_golden_brick.html"

class DonateGeneralView(TemplateView):
    template_name = "donate/donate_general.html"
