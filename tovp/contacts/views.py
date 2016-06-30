# -*- coding: utf-8 -*-
# view imports
from django.views.generic import DetailView, UpdateView, ListView
from django.views.generic.edit import CreateView, DeleteView
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django_ajax.decorators import ajax

# Will be used for logged in and logged out messages
# from django.contrib import messages

# Only authenticated users can access views using this.
from braces.views import (LoginRequiredMixin, PermissionRequiredMixin,
                          MultiplePermissionsRequiredMixin)
from haystack.query import SearchQuerySet
from ananta.models import RevisionCommentMixin

from .models import Person
from .forms import PersonForm


class PersonListView(LoginRequiredMixin, ListView):
    model = Person
    template_name = 'contacts/person_list.html'


class PersonDetailView(LoginRequiredMixin, DetailView):
    model = Person
    template_name = 'contacts/person_detail.html'


class PersonCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Person
    permission_required = "contacts.add_person"
    template_name = 'contacts/person_form.html'
    form_class = PersonForm

    def get_context_data(self, **kwargs):
        context = super(PersonCreateView, self).get_context_data(**kwargs)
        context['content_title'] = _("Add new person")
        return context


class PersonUpdateView(RevisionCommentMixin, LoginRequiredMixin,
                       PermissionRequiredMixin, UpdateView):
    model = Person
    permission_required = "contacts.change_person"
    template_name = 'contacts/person_form.html'
    form_class = PersonForm

    def get_context_data(self, **kwargs):
        context = super(PersonUpdateView, self).get_context_data(**kwargs)
        context['content_title'] = _("Edit contact")
        return context


class PersonDeleteView(MultiplePermissionsRequiredMixin, DeleteView):
    model = Person
    template_name = 'contacts/person_confirm_delete.html'
    permissions = {
        "any": ("contacts.delete_person",
                "contacts.can_delete_if_no_contributions"),
    }
    success_message = "%(pk)s was deleted successfully"

    def dispatch(self, request, *args, **kwargs):
        """
        Check to see if the user in the request has the required
        permission.
        """

        # Check if pledge doesn't have any contributions
        if not self.get_object().can_user_delete(request.user):
            return self.handle_no_permission(request)

        return super(PersonDeleteView, self).dispatch(
            request, *args, **kwargs)

    def get_success_url(self):
        return reverse('search:index')


@ajax
def person_ajax_search(request):
    sqs = SearchQuerySet()
    sqs = sqs.narrow('content_type_exact:"Contact"')

    if 'q' in request.GET:
        q = request.GET['q']
        sqs = sqs.filter(**{'mixed_name__startswith': q})
    return [{'text': "%s (#%d)" % (contact.mixed_name, contact.object.pk),
             'value': contact.object.pk
             } for contact in sqs]
