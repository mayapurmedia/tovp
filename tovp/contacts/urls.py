# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from . import views


person = patterns(
    '',
    # URL pattern for the PersonDetailView
    url(
        regex=r'^(?P<pk>\d+)/$',
        view=views.PersonDetailView.as_view(),
        name='detail',
    ),
    # URL pattern for the PersonCreateView
    url(
        regex=r'^create/$',
        view=views.PersonCreateView.as_view(),
        name='create',
    ),
    # URL pattern for the PersonUpdateView
    url(
        regex=r'^(?P<pk>\d+)/edit$',
        view=views.PersonUpdateView.as_view(),
        name='update',
    ),
)

urlpatterns = patterns(
    '',
    (r'^person/', include(person, namespace="person")),
    # URL pattern for the PersonListView
    url(
        regex=r'^$',
        view=views.PersonListView.as_view(),
        name='index'
    ),
)
