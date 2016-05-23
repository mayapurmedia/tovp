# -*- coding: utf-8 -*-
import json
# Import the reverse lookup function
# from django.core.urlresolvers import reverse

# view imports
from django.views.generic import View, DetailView, UpdateView, ListView
from django.views.generic.edit import CreateView, DeleteView
from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages

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

from .forms import PledgeForm, FollowUpForm, ContributionForm, BulkPaymentForm
from .models import Pledge, FollowUp, Contribution, BulkPayment


class PledgeListView(LoginRequiredMixin, ListView):
    model = Pledge


class PledgeDetailView(LoginRequiredMixin, DetailView):
    model = Pledge
    template_name = 'contributions/pledge_detail.html'

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
    template_name = 'contributions/pledge_confirm_delete.html'
    permissions = {
        "any": ("contributions.delete_pledge",
                "contributions.can_delete_if_no_contributions"),
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


class PledgeAssignToFollow(PermissionRequiredMixin, View):
    permission_required = "contributions.can_follow_pledge"

    def get_object(self):
            return Pledge

    def dispatch(self, request, *args, **kwargs):
        self.pk = kwargs['pk']
        self.pledge = Pledge.objects.get(pk=self.pk)
        self.pledge.assign_follow_up(self.request.user)

        # if this view is called from ajax return json object
        if request.is_ajax():
            if self.pledge.followed_by:
                status_name = self.pledge.followed_by.display_name
            else:
                status_name = 'Nobody'
            response_data = {
                'new_status_name': 'Followed by: ' + status_name,
                'new_status_slug': 'assigned',
            }
            return HttpResponse(json.dumps(response_data),
                                content_type="application/json")

        return HttpResponseRedirect(request.GET['next'])


class FollowUpDetailView(LoginRequiredMixin, DetailView):
    model = FollowUp
    template_name = 'contributions/followup_detail.html'


class FollowUpCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                         CreateView):
    model = FollowUp
    permission_required = "contributions.add_followup"
    template_name = 'contributions/followup_form.html'
    form_class = FollowUpForm

    def get_form_kwargs(self):
        kwargs = super(FollowUpCreateView, self).get_form_kwargs()
        pledge = Pledge.objects.get(pk=self.kwargs.get('pledge_id'))
        next_payment_date = '{0.year}-{0.month}-{0.day}'. \
            format(pledge.update_next_payment_date())
        kwargs['next_payment_date'] = next_payment_date
        return kwargs

    def get_initial(self):
        initial = super(FollowUpCreateView, self).get_initial()
        initial = initial.copy()
        initial['pledge'] = self.kwargs.get('pledge_id')
        return initial

    def get_context_data(self, **kwargs):
        context = super(FollowUpCreateView, self).get_context_data(**kwargs)
        context['content_title'] = _("Add new follow up")
        pledge = Pledge.objects.get(pk=self.kwargs.get('pledge_id'))
        context['pledge'] = pledge
        return context


class FollowUpUpdateView(RevisionCommentMixin, LoginRequiredMixin,
                         PermissionRequiredMixin, UpdateView):
    model = FollowUp
    permission_required = "contributions.change_followup"
    template_name = 'contributions/followup_form.html'
    form_class = FollowUpForm

    def get_context_data(self, **kwargs):
        context = super(FollowUpUpdateView, self).get_context_data(**kwargs)
        context['content_title'] = _("Edit follow up")
        pledge = Pledge.objects.get(pk=self.kwargs.get('pledge_id'))
        context['pledge'] = pledge
        return context


class FollowUpDeleteView(MultiplePermissionsRequiredMixin, DeleteView):
    model = FollowUp
    permission_required = "contributions.delete_followup"
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
    template_name = 'contributions/contribution_list.html'


class ContributionDetailView(LoginRequiredMixin, DetailView):
    model = Contribution
    template_name = 'contributions/contribution_detail.html'


class ContributionConfirmMoveView(LoginRequiredMixin, View):
    template_name = 'contributions/contribution_move.html'

    def post(self, request, *args, **kwargs):
        obj = Contribution.objects.get(pk=kwargs['pk'])
        new_pledge = Pledge.objects.get(pk=request.POST['new_pledge'])

        return render(
            request,
            self.template_name,
            {
                'object': obj,
                'new_pledge': new_pledge,
            }
        )


class ContributionMoveView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "contributions.can_move_contribution"

    def post(self, request, *args, **kwargs):
        obj = Contribution.objects.get(pk=kwargs['pk'])
        old_pledge = obj.pledge
        new_pledge = Pledge.objects.get(pk=request.POST['new_pledge'])
        if not obj.overwrite_name:
            if obj.pledge.person.name:
                obj.overwrite_name = obj.pledge.person.name
            else:
                obj.overwrite_name = obj.pledge.person.initiated_name

        if not obj.overwrite_address:
            address = ''
            for line in obj.pledge.person.full_address():
                if address:
                    address += ', '
                address += line
            obj.overwrite_address = address

        if not obj.overwrite_pan_card:
            obj.overwrite_pan_card = obj.pledge.person.pan_card_number

        obj.pledge = new_pledge
        obj.save()

        messages.success(
            request,
            "You have moved contribution from pledge #%d under pledge #%d" % (
                old_pledge.pk, new_pledge.pk),
            fail_silently=True)

        return redirect(obj)


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

    def get_template_names(self):
        if self.get_object().receipt_type == 'external-receipt':
            raise Http404
        if self.get_object().receipt_type == 'mayapur-receipt':
            return 'contributions/print_contribution_receipt_mayapur.html'
        if self.get_object().receipt_type == 'usa-receipt':
            return 'contributions/print_contribution_receipt_usa.html'

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
        kwargs['request'] = self.request
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
    template_name = 'contributions/bulkpayment_detail.html'


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
