from datetime import datetime, timedelta

from django.apps import apps
from django.urls import reverse
from django.views.generic.base import View, TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from collections import OrderedDict
from django.db.models import ObjectDoesNotExist

from promotions import models

from .models import WebDonation


ENABLED_PROMOTIONS = OrderedDict(
    [
        ('nrsimha-tile', apps.get_model("promotions", "NrsimhaTile")),
        ('golden-brick', apps.get_model("promotions", "GoldenBrick")),
        ('radha-madhava-brick', apps.get_model("promotions", "RadhaMadhavaBrick")),
        ('general-donation', apps.get_model("promotions", "GeneralDonation")),
    ]
)

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

    def get_context_data(self, **kwargs):
        context = super(BaseDonatePromotionView, self).get_context_data(**kwargs)
        currency = REGION_TO_CURRENCY[kwargs['region']]
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

class SaveForm(View):
    def get(self, request, **kwargs):
        print('==================\n\n\n')
        print(kwargs)
        print('------------------')
        # my_data = request.POST
        # context = {}  #  set your context
        return HttpResponseRedirect(reverse('donate:donate'))

    def post(self, request, **kwargs):
        data = request.POST
        print('==================\n\n\n')
        print(kwargs)
        print('==================\n\n\n')
        print(data)
        print('------------------')
        promotion = ENABLED_PROMOTIONS[kwargs['promotion_slug']]
        currency = REGION_TO_CURRENCY[kwargs['region']]
        print(promotion.amount_grid[currency['code']])
        print(currency)
        print('------------------')
        # '''
        # 'amount-other-value': [''],
        # 'amount': ['5'],
        # '''
        web_donation = None
        # tries to load WebDonation which is created less then 15 minutes ago
        # and have same csrf_token as current post
        try:
            web_donation = WebDonation.objects.get(
                csrf_token=data['csrfmiddlewaretoken'],
                modified__lte=datetime.now() - timedelta(seconds=900))
        except ObjectDoesNotExist:
            web_donation = WebDonation()
            print('creating.............')

        web_donation.phone_number = data['phone']
        web_donation.address = data['address']
        web_donation.first_name = data['first-name']
        web_donation.last_name = data['last-name']
        web_donation.email = data['email']
        web_donation.csrf_token = data['csrfmiddlewaretoken']
        web_donation.amount = data['amount']
        web_donation.initiated_name = data['initiated-name']
        # 'email': ['prahlad@vedabase.com'],
        # web_donation.save()
        # context = {}  #  set your context
        return HttpResponse('Here we should save data and redirect to payment method')
