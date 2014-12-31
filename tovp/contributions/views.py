# -*- coding: utf-8 -*-
# Import the reverse lookup function
# from django.core.urlresolvers import reverse

# view imports
from django.views.generic import DetailView
# from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from django.utils.translation import ugettext as _
# from django.shortcuts import get_object_or_404

# Will be used for logged in and logged out messages
# from django.contrib import messages

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin

from .forms import ContributionForm
from .models import Contribution


class ContributionListView(LoginRequiredMixin, ListView):
    model = Contribution


class ContributionDetailView(LoginRequiredMixin, DetailView):
    model = Contribution


class ContributionDonorLetterDetailView(LoginRequiredMixin, DetailView):
    model = Contribution
    template_name = 'contributions/print_donor_letter.html'


class DonorInvoiceDetailView(LoginRequiredMixin, DetailView):
    model = Contribution
    template_name = 'contributions/print_donor_invoice.html'


class ContributionCreateView(LoginRequiredMixin, CreateView):
    model = Contribution
    template_name = 'contributions/contribution_form.html'
    form_class = ContributionForm

    def get_initial(self):
        initial = super(ContributionCreateView, self).get_initial()
        initial = initial.copy()
        initial['person'] = self.kwargs.get('person_id')  # self.request.user.pk
        return initial

    def get_context_data(self, **kwargs):
        context = super(ContributionCreateView, self).get_context_data(**kwargs)
        context['content_title'] = _("Add new contribution")
        return context


class ContributionUpdateView(LoginRequiredMixin, UpdateView):
    model = Contribution
    template_name = 'contributions/contribution_form.html'
    form_class = ContributionForm

    def get_context_data(self, **kwargs):
        context = super(ContributionUpdateView, self).get_context_data(**kwargs)
        context['content_title'] = _("Edit contribution")
        return context
