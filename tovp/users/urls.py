# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    # URL pattern for the UserListView  # noqa
    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),
    # URL pattern for the UserRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),
    # URl pattern for login view
    url(r'^login/$', auth_views.login,
        {'template_name': 'registration/login.html'},
        name="login"),
    # URl pattern for logout view
    url(r'^logout/$', auth_views.logout,
        {'next_page': '/'}, name="logout"),
    # URL pattern for the UserDetailView
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
    # URL pattern for the UserUpdateView
    url(
        regex=r'^~update/$',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),
    url(r'^password/reset/$',
        auth_views.password_reset,
        {
            'post_reset_redirect': '/users/password/reset/done/',
        },
        name="password_reset"),
    url(r'^password/reset/done/$',
        auth_views.password_reset_done),
    url(
        regex=r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        view=auth_views.password_reset_confirm,
        kwargs={'post_reset_redirect': '/users/password/done/'},
        name='password_reset_confirm',
    ),
    url(r'^password/done/$',
        auth_views.password_reset_complete),
]
