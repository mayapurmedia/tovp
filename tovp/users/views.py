# -*- coding: utf-8 -*-
# Import the reverse lookup function
from django.core.urlresolvers import reverse

# view imports
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView

# Will be used for logged in and logged out messages
from django.contrib import messages
from django.contrib.auth.signals import user_logged_in, user_logged_out

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin

# Import the form from users/forms.py
from .forms import UserUpdateForm

# Import the customized User model
from .models import User


class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'users/user_detail.jinja'
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    model = User
    template_name = 'users/user_update.jinja'

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("users:redirect")

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)

    def form_valid(self, form):
        # Sets new password if user defined one
        if form.cleaned_data['password1']:
            form.instance.set_password(form.cleaned_data['password1'])
            messages.success(self.request, 'Your Account Settings has been saved.')
        return super(UserUpdateView, self).form_valid(form)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


def logged_in_message(sender, user, request, **kwargs):
    messages.success(
        request,
        "Welcome, %s! You have been successfully logged in." % user.display_name,
        fail_silently=True)

user_logged_in.connect(logged_in_message)


def logged_out_message(sender, user, request, **kwargs):
    messages.success(request, "You have been successfully logged out.",
                     fail_silently=True)

user_logged_out.connect(logged_out_message)
