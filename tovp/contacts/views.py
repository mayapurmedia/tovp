# -*- coding: utf-8 -*-
# view imports
from django.views.generic import DetailView, UpdateView, ListView
from django.views.generic.edit import CreateView

from django.utils.translation import ugettext as _
from django_ajax.decorators import ajax

# Will be used for logged in and logged out messages
# from django.contrib import messages

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from haystack.query import SearchQuerySet
from ananta.models import RevisionCommentMixin

from .models import Person
from .forms import PersonForm


class PersonListView(LoginRequiredMixin, ListView):
    model = Person


class PersonDetailView(LoginRequiredMixin, DetailView):
    model = Person


class PersonCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Person
    permission_required = "contacts.add_person"
    template_name = 'contacts/person_form.jinja'
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
