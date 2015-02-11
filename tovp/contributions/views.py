# -*- coding: utf-8 -*-
# Import the reverse lookup function
# from django.core.urlresolvers import reverse

# view imports
from django.views.generic import DetailView, UpdateView, ListView
from django.views.generic.edit import CreateView, DeleteView
from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404

# Will be used for logged in and logged out messages
# from django.contrib import messages

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin

from ananta.models import RevisionCommentMixin

from .forms import PledgeForm, ContributionForm
from .models import Pledge, Contribution


class PledgeListView(LoginRequiredMixin, ListView):
    model = Pledge


class PledgeDetailView(LoginRequiredMixin, DetailView):
    model = Pledge


class PledgeCreateView(LoginRequiredMixin, CreateView):
    model = Pledge
    template_name = 'contributions/pledge_form.html'
    form_class = PledgeForm

    def get_initial(self):
        initial = super(PledgeCreateView, self).get_initial()
        initial = initial.copy()
        initial['person'] = self.kwargs.get('person_id')
        return initial

    def get_context_data(self, **kwargs):
        context = super(PledgeCreateView, self).get_context_data(**kwargs)
        context['content_title'] = _("Add new pledge")
        return context


class PledgeUpdateView(RevisionCommentMixin, LoginRequiredMixin, UpdateView):
    model = Pledge
    template_name = 'contributions/pledge_form.html'
    form_class = PledgeForm

    def get_context_data(self, **kwargs):
        context = super(PledgeUpdateView, self).get_context_data(**kwargs)
        context['content_title'] = _("Edit pledge")
        return context


class PledgeDeleteView(DeleteView):
    model = Pledge
    success_message = "%(pk)s was deleted successfully"

    def get_success_url(self):
        item = get_object_or_404(Pledge, pk=self.kwargs['pk'])
        return item.person.get_absolute_url()


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

    def get_form_kwargs(self):
        kwargs = super(ContributionCreateView, self).get_form_kwargs()
        kwargs['person'] = self.kwargs.get('person_id')
        return kwargs

    def get_initial(self):
        initial = super(ContributionCreateView, self).get_initial()
        initial = initial.copy()
        initial['person'] = self.kwargs.get('person_id')
        initial['pledge'] = self.kwargs.get('pledge_id')
        return initial

    def get_context_data(self, **kwargs):
        context = super(ContributionCreateView, self).get_context_data(**kwargs)
        context['content_title'] = _("Add new contribution")
        return context


class ContributionUpdateView(RevisionCommentMixin, LoginRequiredMixin, UpdateView):
    model = Contribution
    template_name = 'contributions/contribution_form.html'
    form_class = ContributionForm

    def get_form_kwargs(self):
        kwargs = super(ContributionUpdateView, self).get_form_kwargs()
        kwargs['person'] = self.kwargs.get('person_id')
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(ContributionUpdateView, self).get_context_data(**kwargs)
        context['content_title'] = _("Edit contribution")
        return context


class ContributionDeleteView(DeleteView):
    model = Contribution
    success_message = "%(pk)s was deleted successfully"
    template_name = 'contributions/model_confirm_delete.html'

    def get_success_url(self):
        item = get_object_or_404(Contribution, pk=self.kwargs['pk'])
        return item.person.get_absolute_url()
