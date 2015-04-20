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
from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from ananta.models import RevisionCommentMixin
from promotions.models import promotions

from .forms import PledgeForm, ContributionForm, BulkPaymentForm
from .models import Pledge, Contribution, BulkPayment


class PledgeListView(LoginRequiredMixin, ListView):
    model = Pledge


class PledgeDetailView(LoginRequiredMixin, DetailView):
    model = Pledge

    def get_context_data(self, **kwargs):
        context = super(PledgeDetailView, self).get_context_data(**kwargs)
        ballance = self.get_object().person.get_ballance()
        promotions_eligible = []
        promotions_not_eligible = []
        for promotion in promotions:
            if promotion.is_eligible(ballance):
                promotions_eligible.append(promotion)
            else:
                promotions_not_eligible.append(promotion)
        context['eligible_promotions'] = promotions_eligible
        context['not_eligible_promotions'] = promotions_not_eligible
        return context


class PledgeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Pledge
    permission_required = "contributions.add_pledge"
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


class PledgeUpdateView(RevisionCommentMixin, LoginRequiredMixin,
                       PermissionRequiredMixin, UpdateView):
    model = Pledge
    permission_required = "contributions.change_pledge"
    template_name = 'contributions/pledge_form.html'
    form_class = PledgeForm

    def get_context_data(self, **kwargs):
        context = super(PledgeUpdateView, self).get_context_data(**kwargs)
        context['content_title'] = _("Edit pledge")
        return context


class PledgeDeleteView(PermissionRequiredMixin, DeleteView):
    model = Pledge
    permission_required = "contributions.delete_pledge"
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
    print_signature = None
    model = Contribution
    template_name = 'contributions/print_donor_invoice.html'

    def get_context_data(self, **kwargs):
        context = super(DonorInvoiceDetailView, self).get_context_data(
            **kwargs)
        context['print_signature'] = self.print_signature
        return context


class ContributionCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                             CreateView):
    model = Contribution
    permission_required = "contributions.add_contribution"
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


class ContributionUpdateView(RevisionCommentMixin, LoginRequiredMixin,
                             PermissionRequiredMixin, UpdateView):
    model = Contribution
    permission_required = "contributions.change_contribution"
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

    def form_valid(self, form):
        instance = form.save(commit=False)
        # Set contribution's receipt to be external when saved by user who can
        # save only external receipts
        if (self.request.user.only_external_receipts):
            instance.is_external = True
            self.object = form.save()
        return super(ContributionUpdateView, self).form_valid(form)


class ContributionDeleteView(PermissionRequiredMixin, DeleteView):
    model = Contribution
    permission_required = "contributions.delete_contribution"
    success_message = "%(pk)s was deleted successfully"
    template_name = 'contributions/model_confirm_delete.html'

    def get_success_url(self):
        item = get_object_or_404(Contribution, pk=self.kwargs['pk'])
        return item.pledge.person.get_absolute_url()


class BulkPaymentDetailView(LoginRequiredMixin, DetailView):
    model = BulkPayment


class BulkPaymentCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                            CreateView):
    model = BulkPayment
    permission_required = "contributions.add_contribution"
    template_name = 'contributions/bulkpayment_form.html'
    form_class = BulkPaymentForm

    def get_form_kwargs(self):
        kwargs = super(BulkPaymentCreateView, self).get_form_kwargs()
        kwargs['person'] = self.kwargs.get('person_id')
        return kwargs

    def get_initial(self):
        initial = super(BulkPaymentCreateView, self).get_initial()
        initial = initial.copy()
        initial['person'] = self.kwargs.get('person_id')
        return initial

    def get_context_data(self, **kwargs):
        context = super(BulkPaymentCreateView, self).get_context_data(**kwargs)
        context['content_title'] = _("Add new bulk payment")
        return context


class BulkPaymentUpdateView(RevisionCommentMixin, LoginRequiredMixin,
                            PermissionRequiredMixin, UpdateView):
    model = BulkPayment
    permission_required = "contributions.change_bulkpayment"
    template_name = 'contributions/bulkpayment_form.html'
    form_class = BulkPaymentForm

    def get_form_kwargs(self):
        kwargs = super(BulkPaymentUpdateView, self).get_form_kwargs()
        kwargs['person'] = self.kwargs.get('person_id')
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(BulkPaymentUpdateView, self).get_context_data(**kwargs)
        context['content_title'] = _("Edit bulk payment")
        return context


class BulkPaymentDeleteView(PermissionRequiredMixin, DeleteView):
    model = BulkPayment
    permission_required = "contributions.delete_bulkpayment"
    success_message = "%(pk)s was deleted successfully"
    template_name = 'contributions/model_confirm_delete.html'

    def get_success_url(self):
        item = get_object_or_404(BulkPayment, pk=self.kwargs['pk'])
        return item.person.get_absolute_url()


class BulkPaymentReceiptDetailView(LoginRequiredMixin, DetailView):
    print_signature = None
    model = BulkPayment
    template_name = 'contributions/print_collector_invoice.html'

    def get_context_data(self, **kwargs):
        context = super(BulkPaymentReceiptDetailView, self).get_context_data(
            **kwargs)
        context['print_signature'] = self.print_signature
        return context
