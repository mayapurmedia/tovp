# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from . import views


pledges = patterns(
    '',
    url(
        regex=r'^$',
        view=views.PledgeListView.as_view(),
        name='index'
    ),
    url(
        regex=r'^(?P<person_id>\d+)/(?P<pk>\d+)/$',
        view=views.PledgeDetailView.as_view(),
        name='detail',
    ),
    url(
        regex=r'^(?P<person_id>\d+)/create/$',
        view=views.PledgeCreateView.as_view(),
        name='create',
    ),
    url(
        regex=r'^(?P<person_id>\d+)/(?P<pk>\d+)/edit$',
        view=views.PledgeUpdateView.as_view(),
        name='update',
    ),
    url(
        regex=r'^delete/(?P<pk>\d+)/$',
        view=views.PledgeDeleteView.as_view(),
        name="delete",
    ),
)

contributions = patterns(
    '',
    url(
        regex=r'^$',
        view=views.ContributionListView.as_view(),
        name='index'
    ),
    url(
        regex=r'^(?P<person_id>\d+)/(?P<pk>\d+)/$',
        view=views.ContributionDetailView.as_view(),
        name='detail',
    ),
    url(
        regex=r'^(?P<person_id>\d+)/create/$',
        view=views.ContributionCreateView.as_view(),
        name='create',
    ),
    # create new contribution with auto filled pledge
    url(
        regex=r'^(?P<person_id>\d+)/(?P<pledge_id>\d+)/create/$',
        view=views.ContributionCreateView.as_view(),
        name='create',
    ),
    url(
        regex=r'^(?P<person_id>\d+)/(?P<pk>\d+)/edit$',
        view=views.ContributionUpdateView.as_view(),
        name='update',
    ),
    url(
        regex=r'^print/(?P<pk>\d+)/donor$',
        view=views.ContributionDonorLetterDetailView.as_view(),
        name='donor_letter',
    ),
    url(
        regex=r'^print/(?P<pk>\d+)/receipt$',
        view=views.DonorInvoiceDetailView.as_view(),
        name='donor_receipt',
    ),
    url(
        regex=r'^delete/(?P<pk>\d+)/$',
        view=views.ContributionDeleteView.as_view(),
        name="delete",
    ),
)


urlpatterns = patterns(
    '',
    (r'^pledge/', include(pledges, namespace="pledge")),
    (r'^contribution/', include(contributions, namespace="contribution")),
)
