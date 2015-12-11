# -*- coding: utf-8 -*-
# view imports
from django.views.generic import DetailView, UpdateView, ListView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib import messages
from django.utils.translation import ugettext as _

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from ananta.models import RevisionCommentMixin
from contacts.models import Person

from .models import Gift, GiftGiven
from .forms import GiftForm, GiftGivenForm


class GiftListView(LoginRequiredMixin, ListView):
    model = Gift


class GiftDetailView(LoginRequiredMixin, DetailView):
    model = Gift


class GiftCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Gift
    permission_required = "gifts.add_gift"
    template_name = 'gifts/gift_form.jinja'
    form_class = GiftForm

    def get_context_data(self, **kwargs):
        context = super(GiftCreateView, self).get_context_data(**kwargs)
        context['content_title'] = _("Add new gift")
        return context


class GiftUpdateView(RevisionCommentMixin, LoginRequiredMixin,
                     PermissionRequiredMixin, UpdateView):
    model = Gift
    permission_required = "gifts.change_gift"
    template_name = 'gifts/gift_form.jinja'
    form_class = GiftForm

    def get_context_data(self, **kwargs):
        context = super(GiftUpdateView, self).get_context_data(**kwargs)
        context['content_title'] = _("Edit gift")
        return context


class GiftGivenDetailView(LoginRequiredMixin, DetailView):
    model = GiftGiven
    template_name = 'gifts/gift_given_detail.jinja'


class GiftGivenCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                          CreateView):
    model = GiftGiven
    permission_required = "gifts.add_giftgiven"
    template_name = 'gifts/gift_given_form.jinja'
    form_class = GiftGivenForm

    def get_initial(self):
        initial = super(GiftGivenCreateView, self).get_initial()
        initial = initial.copy()
        initial['person'] = self.kwargs.get('person_id')
        return initial

    def get_context_data(self, **kwargs):
        context = super(GiftGivenCreateView, self).get_context_data(**kwargs)
        context['content_title'] = _("Add new gift")
        person = Person.objects.get(pk=self.kwargs.get('person_id'))
        context['person'] = person
        return context


class GiftGivenUpdateView(RevisionCommentMixin, LoginRequiredMixin,
                          PermissionRequiredMixin, UpdateView):
    model = GiftGiven
    permission_required = "gifts.change_giftgiven"
    template_name = 'gifts/gift_given_form.jinja'
    form_class = GiftGivenForm

    def get_context_data(self, **kwargs):
        context = super(GiftGivenUpdateView, self).get_context_data(**kwargs)
        context['content_title'] = _("Edit gift")
        person = Person.objects.get(pk=self.kwargs.get('person_id'))
        context['person'] = person
        return context


class GiftGivenDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "gifts.delete_giftgiven"
    template_name = 'promotions/confirm_delete.jinja'
    model = GiftGiven

    def get_success_url(self):
        return self.get_object().person.get_absolute_url()

    def delete(self, request, *args, **kwargs):
        success_message = "%s has been deleted successfully" % \
            self.get_object()._meta.verbose_name.title()
        messages.success(self.request, success_message)
        return super(GiftGivenDeleteView, self).delete(request, *args, **kwargs)
