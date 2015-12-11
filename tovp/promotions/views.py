# -*- coding: utf-8 -*-
# Import the reverse lookup function
# from django.core.urlresolvers import reverse

# view imports
from django.views.generic import DetailView, UpdateView  # , ListView
from django.views.generic.edit import CreateView, DeleteView
# from django.utils.translation import ugettext as _
# from django.shortcuts import get_object_or_404

# Will be used for logged in and logged out messages
from django.contrib import messages

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin, PermissionRequiredMixin


class BasePromotionCreateUpdateView(LoginRequiredMixin,
                                    PermissionRequiredMixin):
    template_name = 'promotions/promotion_form.jinja'
    permission_required = "promotions.add_nrsimhatile"

    def get_form_kwargs(self):
        kwargs = super(BasePromotionCreateUpdateView, self).get_form_kwargs()
        kwargs['person'] = self.kwargs.get('person_id')
        return kwargs

    def get_success_url(self):
        return self.object.pledge.get_absolute_url()

    def get_initial(self):
        initial = super(BasePromotionCreateUpdateView, self).get_initial()
        initial = initial.copy()
        initial['person'] = self.kwargs.get('person_id')
        initial['pledge'] = self.kwargs.get('pledge_id')
        return initial

    def get_context_data(self, **kwargs):
        context = super(BasePromotionCreateUpdateView, self).get_context_data(
            **kwargs)
        context['content_title'] = "Add %s" % self.model._meta. \
            verbose_name.title()
        context['complimentary_bricks'] = ['nrsimha_tile', 'golden_brick',
                                           'radha_madhava_brick']
        return context


class BasePromotionCreateView(BasePromotionCreateUpdateView, CreateView):
    pass


class BasePromotionUpdateView(BasePromotionCreateUpdateView, UpdateView):
    pass


class PromotionDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "promotions.delete_nrsimhatile"
    template_name = 'promotions/confirm_delete.jinja'

    def get_success_url(self):
        return self.get_object().pledge.get_absolute_url()

    def delete(self, request, *args, **kwargs):
        success_message = "%s has been deleted successfully" % \
            self.get_object()._meta.verbose_name.title()
        messages.success(self.request, success_message)
        return super(PromotionDeleteView, self).delete(request, *args, **kwargs)


class BrickCreateView(BasePromotionCreateView):
    template_name = 'promotions/brick_form.jinja'


class BrickUpdateView(BasePromotionUpdateView):
    template_name = 'promotions/brick_form.jinja'


class BrickDetailView(DetailView):
    template_name = 'promotions/brick_detail.jinja'


class CoinCreateView(BasePromotionCreateView):
    template_name = 'promotions/coin_form.jinja'


class CoinUpdateView(BasePromotionUpdateView):
    template_name = 'promotions/coin_form.jinja'


class CoinDetailView(DetailView):
    template_name = 'promotions/coin_detail.jinja'


class FeetCreateView(BasePromotionCreateView):
    template_name = 'promotions/feet_form.jinja'


class FeetUpdateView(BasePromotionUpdateView):
    template_name = 'promotions/feet_form.jinja'


class FeetDetailView(DetailView):
    template_name = 'promotions/feet_detail.jinja'


class TrusteeCreateView(BasePromotionCreateView):
    template_name = 'promotions/promotion_form.jinja'


class TrusteeUpdateView(BasePromotionUpdateView):
    template_name = 'promotions/promotion_form.jinja'


class TrusteeDetailView(DetailView):
    template_name = 'promotions/promotion_detail.jinja'


class GeneralDonationCreateView(BasePromotionCreateView):
    template_name = 'promotions/promotion_form.jinja'


class GeneralDonationUpdateView(BasePromotionUpdateView):
    template_name = 'promotions/promotion_form.jinja'


class GeneralDonationDetailView(DetailView):
    template_name = 'promotions/promotion_detail.jinja'
