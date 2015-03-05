# -*- coding: utf-8 -*-
# Import the reverse lookup function
# from django.core.urlresolvers import reverse

# view imports
# from django.views.generic import DetailView, UpdateView, ListView
from django.views.generic.edit import CreateView  # , DeleteView
# from django.utils.translation import ugettext as _
# from django.shortcuts import get_object_or_404

# Will be used for logged in and logged out messages
# from django.contrib import messages

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from .models import (NrsimhaTile, GoldenBrick, GuruParamparaBrick,
                     RadhaMadhavaBrick, SilverCoin, GoldCoin, PlatinumCoin,
                     SquareFeet, SquareMeter, Trustee, GeneralDonation)

from .forms import (NrsimhaTileForm, GoldenBrickForm, GuruParamparaBrickForm,
                    RadhaMadhavaBrickForm, SilverCoinForm, GoldCoinForm,
                    PlatinumCoinForm, SquareFeetForm, SquareMeterForm,
                    TrusteeForm, GeneralDonationForm)


class BasePromotionCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                              CreateView):
    template_name = 'promotions/promotion_form.html'
    permission_required = "promotions.add_nrsimhatile"

    def get_form_kwargs(self):
        kwargs = super(BasePromotionCreateView, self).get_form_kwargs()
        kwargs['person'] = self.kwargs.get('person_id')
        return kwargs

    def get_success_url(self):
        return self.object.pledge.get_absolute_url()

    def get_initial(self):
        initial = super(BasePromotionCreateView, self).get_initial()
        initial = initial.copy()
        initial['person'] = self.kwargs.get('person_id')
        initial['pledge'] = self.kwargs.get('pledge_id')
        return initial

    def get_context_data(self, **kwargs):
        context = super(BasePromotionCreateView, self).get_context_data(
            **kwargs)
        context['content_title'] = "Add %s" % self.model._meta. \
            verbose_name.title()
        return context


class BaseBrickCreateView(BasePromotionCreateView):
    template_name = 'promotions/brick_form.html'


class NrsimhaTileCreateView(BaseBrickCreateView):
    model = NrsimhaTile
    form_class = NrsimhaTileForm


class GoldenBrickCreateView(BaseBrickCreateView):
    model = GoldenBrick
    form_class = GoldenBrickForm


class GuruParamparaBrickCreateView(BaseBrickCreateView):
    model = GuruParamparaBrick
    form_class = GuruParamparaBrickForm


class RadhaMadhavaBrickCreateView(BaseBrickCreateView):
    model = RadhaMadhavaBrick
    form_class = RadhaMadhavaBrickForm


class BaseCoinCreateView(BasePromotionCreateView):
    template_name = 'promotions/coin_form.html'


class SilverCoinCreateView(BaseCoinCreateView):
    model = SilverCoin
    form_class = SilverCoinForm


class GoldCoinCreateView(BaseCoinCreateView):
    model = GoldCoin
    form_class = GoldCoinForm


class PlatinumCoinCreateView(BaseCoinCreateView):
    model = PlatinumCoin
    form_class = PlatinumCoinForm


class SquareFeetCreateView(BasePromotionCreateView):
    template_name = 'promotions/square_feet_form.html'
    model = SquareFeet
    form_class = SquareFeetForm


class SquareMeterCreateView(BasePromotionCreateView):
    template_name = 'promotions/square_feet_form.html'
    model = SquareMeter
    form_class = SquareMeterForm


class TrusteeCreateView(BasePromotionCreateView):
    model = Trustee
    form_class = TrusteeForm


class GeneralDonationCreateView(BasePromotionCreateView):
    model = GeneralDonation
    form_class = GeneralDonationForm
