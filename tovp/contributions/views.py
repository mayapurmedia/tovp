# -*- coding: utf-8 -*-
import json
# Import the reverse lookup function
# from django.core.urlresolvers import reverse

# view imports
from django.views.generic import View, DetailView, UpdateView, ListView
from django.views.generic.edit import CreateView, DeleteView
from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

# Will be used for logged in and logged out messages
# from django.contrib import messages

# Only authenticated users can access views using this.
from braces.views import (LoginRequiredMixin, PermissionRequiredMixin,
                          MultiplePermissionsRequiredMixin)
from haystack.query import SearchQuerySet
from django_ajax.decorators import ajax

from ananta.models import RevisionCommentMixin
from promotions.models import promotions

from contacts.models import Person

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
        person = Person.objects.get(pk=self.kwargs.get('person_id'))
        context['person'] = person
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
        person = Person.objects.get(pk=self.kwargs.get('person_id'))
        context['person'] = person
        return context


class PledgeDeleteView(MultiplePermissionsRequiredMixin, DeleteView):
    model = Pledge
    permissions = {
        "any": ("contributions.delete_pledge", "contributions.can_delete_if_no_contributions"),
    }
    success_message = "%(pk)s was deleted successfully"

    def dispatch(self, request, *args, **kwargs):
        """
        Check to see if the user in the request has the required
        permission.
        """

        # Check if pledge doesn't have any contributions
        if not self.get_object().can_delete_pledge(request.user):
            return self.handle_no_permission(request)

        return super(PledgeDeleteView, self).dispatch(
            request, *args, **kwargs)

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

    def get_context_data(self, **kwargs):
        context = super(ContributionDonorLetterDetailView, self). \
            get_context_data(**kwargs)
        context['person'] = self.get_object().pledge.person
        return context


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
        person = Person.objects.get(pk=self.kwargs.get('person_id'))
        context['person'] = person
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
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(ContributionUpdateView, self).get_context_data(**kwargs)
        context['content_title'] = _("Edit contribution")
        person = Person.objects.get(pk=self.kwargs.get('person_id'))
        context['person'] = person
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


class ContributionDepositStatusChangeView(PermissionRequiredMixin, View):
    permission_required = "contributions.can_deposit"

    def get_object(self):
            return Contribution

    def dispatch(self, request, *args, **kwargs):
        self.pk = kwargs['pk']
        self.contribution = Contribution.objects.get(pk=self.pk)
        self.contribution.change_deposited_status(self.request.user)

        # if this view is called from ajax return json object
        if request.is_ajax():
            response_data = {
                'new_status_name': self.contribution.get_deposited_status_display(),
                'new_status_slug': self.contribution.deposited_status,
            }
            return HttpResponse(json.dumps(response_data),
                                content_type="application/json")

        return HttpResponseRedirect(request.GET['next'])


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
    model = BulkPayment
    template_name = 'contributions/print_collector_invoice.html'

    def get_context_data(self, **kwargs):
        context = super(BulkPaymentReceiptDetailView, self).get_context_data(
            **kwargs)
        if self.kwargs['signature'] == '1':
            print_signature = True
        else:
            print_signature = None
        context['print_signature'] = print_signature
        return context


class BulkPaymentDonorLetterDetailView(LoginRequiredMixin, DetailView):
    model = BulkPayment
    template_name = 'contributions/print_donor_letter.html'

    def get_context_data(self, **kwargs):
        context = super(BulkPaymentDonorLetterDetailView, self). \
            get_context_data(**kwargs)
        context['person'] = self.get_object().person
        return context


@ajax
def bulk_payment_ajax_search(request):
    sqs = SearchQuerySet()
    sqs = sqs.narrow('content_type_exact:"Bulk Payment"')

    if 'q' in request.GET:
        q = request.GET['q']
        sqs = sqs.filter(**{'mixed_name__startswith': q})
    return [{
        'text': "(#%d) %s %d%s %s" % (
            bulk_payment.object.pk,
            bulk_payment.object.person.mixed_name,
            bulk_payment.amount,
            bulk_payment.currency,
            bulk_payment.receipt_date.strftime("(%B %-d %Y)"),
        ),
        'value': bulk_payment.object.pk
    } for bulk_payment in sqs]
