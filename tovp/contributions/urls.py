# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    # URL pattern for the ContributionListView
    url(
        regex=r'^$',
        view=views.ContributionListView.as_view(),
        name='index'
    ),
    # URL pattern for the ContributionDetailView
    url(
        regex=r'^(?P<person_id>\d+)/(?P<pk>\d+)/$',
        view=views.ContributionDetailView.as_view(),
        name='detail',
    ),
    # URL pattern for the ContributionCreateView
    url(
        regex=r'^(?P<person_id>\d+)/create/$',
        view=views.ContributionCreateView.as_view(),
        name='create',
    ),
    # URL pattern for the ContributionUpdateView
    url(
        regex=r'^(?P<person_id>\d+)/(?P<pk>\d+)/edit$',
        view=views.ContributionUpdateView.as_view(),
        name='update',
    ),
    # URL pattern for the ContributionDetailView
    url(
        regex=r'^print/(?P<pk>\d+)/donor$',
        view=views.ContributionDonorLetterDetailView.as_view(),
        name='donor_letter',
    ),
    # URL pattern for the ContributionDetailView
    url(
        regex=r'^print/(?P<pk>\d+)/receipt$',
        view=views.DonorInvoiceDetailView.as_view(),
        name='donor_receipt',
    ),
)
