# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from users import views


urlpatterns = patterns('',
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
    url(r'^login/$', 'django.contrib.auth.views.login',
        name="login"),
    # URl pattern for logout view
    url(r'^logout/$', 'django.contrib.auth.views.logout',
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
        'django.contrib.auth.views.password_reset',
        {
            'post_reset_redirect': '/users/password/reset/done/',
        },
        name="password_reset"),
    (r'^password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    url(
        regex=r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        view='django.contrib.auth.views.password_reset_confirm',
        kwargs={'post_reset_redirect': '/users/password/done/'},
        name='password_reset_confirm',
    ),
    (r'^password/done/$',
        'django.contrib.auth.views.password_reset_complete'),
)
