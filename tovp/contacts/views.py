# -*- coding: utf-8 -*-
# view imports
from django.views.generic import DetailView
# from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from django.utils.translation import ugettext as _

# Will be used for logged in and logged out messages
# from django.contrib import messages

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin

# Import the customized Person model
from .models import Person
from .forms import PersonForm


class PersonListView(LoginRequiredMixin, ListView):
    model = Person


class PersonDetailView(LoginRequiredMixin, DetailView):
    model = Person


class PersonCreateView(LoginRequiredMixin, CreateView):
    model = Person
    template_name = 'contacts/person_form.html'
    form_class = PersonForm

    def get_context_data(self, **kwargs):
        context = super(PersonCreateView, self).get_context_data(**kwargs)
        context['content_title'] = _("Add new person")
        return context


class PersonUpdateView(LoginRequiredMixin, UpdateView):
    model = Person
    template_name = 'contacts/person_form.html'
    form_class = PersonForm

    def get_context_data(self, **kwargs):
        context = super(PersonUpdateView, self).get_context_data(**kwargs)
        context['content_title'] = _("Edit contact")
        return context
