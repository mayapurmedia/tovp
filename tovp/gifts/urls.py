# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from . import views


gift = patterns(
    '',
    url(
        regex=r'^$',
        view=views.GiftListView.as_view(),
        name='index'
    ),
    # URL pattern for the GiftDetailView
    url(
        regex=r'^(?P<pk>\d+)/$',
        view=views.GiftDetailView.as_view(),
        name='detail',
    ),
    # URL pattern for the GiftCreateView
    url(
        regex=r'^create/$',
        view=views.GiftCreateView.as_view(),
        name='create',
    ),
    # URL pattern for the GiftUpdateView
    url(
        regex=r'^(?P<pk>\d+)/edit$',
        view=views.GiftUpdateView.as_view(),
        name='update',
    ),
)

gift_given = patterns(
    '',
    # URL pattern for the GiftDetailView
    url(
        regex=r'^(?P<pk>\d+)/$',
        view=views.GiftGivenDetailView.as_view(),
        name='detail',
    ),
    # URL pattern for the GiftCreateView
    url(
        regex=r'^create/(?P<person_id>\d+)/$',
        view=views.GiftGivenCreateView.as_view(),
        name='create',
    ),
    # URL pattern for the GiftUpdateView
    url(
        regex=r'^(?P<person_id>\d+)/(?P<pk>\d+)/edit$',
        view=views.GiftGivenUpdateView.as_view(),
        name='update',
    ),
    url(
        regex=r'^delete/(?P<pk>\d+)/$',
        view=views.GiftGivenDeleteView.as_view(),
        name="delete",
    ),
)

urlpatterns = patterns(
    '',
    (r'^gift/', include(gift, namespace="gift")),
    (r'^gift_given/', include(gift_given, namespace="gift_given")),
)
