# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from . import views


urlpatterns = patterns(
    '',
    (r'^nrsimha_tile/', include(
        patterns(
            '',
            url(
                regex=r'^(?P<person_id>\d+)/create/$',
                view=views.NrsimhaTileCreateView.as_view(),
                name='create'
            ),
        ), namespace="nrsimha_tile")),
    (r'^golden_brick/', include(
        patterns(
            '',
            url(
                regex=r'^(?P<person_id>\d+)/create/$',
                view=views.GoldenBrickCreateView.as_view(),
                name='create'
            ),
        ), namespace="golden_brick")),
    (r'^radha_madhava_brick/', include(
        patterns(
            '',
            url(
                regex=r'^(?P<person_id>\d+)/create/$',
                view=views.RadhaMadhavaBrickCreateView.as_view(),
                name='create'
            ),
        ), namespace="radha_madhava_brick")),
    (r'^silver_coin/', include(
        patterns(
            '',
            url(
                regex=r'^(?P<person_id>\d+)/create/$',
                view=views.SilverCoinCreateView.as_view(),
                name='create'
            ),
        ), namespace="silver_coin")),
    (r'^gold_coin/', include(
        patterns(
            '',
            url(
                regex=r'^(?P<person_id>\d+)/create/$',
                view=views.GoldCoinCreateView.as_view(),
                name='create'
            ),
        ), namespace="gold_coin")),
    (r'^platinum_coin/', include(
        patterns(
            '',
            url(
                regex=r'^(?P<person_id>\d+)/create/$',
                view=views.PlatinumCoinCreateView.as_view(),
                name='create'
            ),
        ), namespace="platinum_coin")),
    (r'^square_feet/', include(
        patterns(
            '',
            url(
                regex=r'^(?P<person_id>\d+)/create/$',
                view=views.SquareFeetCreateView.as_view(),
                name='create'
            ),
        ), namespace="square_feet")),
    (r'^square_meter/', include(
        patterns(
            '',
            url(
                regex=r'^(?P<person_id>\d+)/create/$',
                view=views.SquareMeterCreateView.as_view(),
                name='create'
            ),
        ), namespace="square_meter")),
    (r'^trustee/', include(
        patterns(
            '',
            url(
                regex=r'^(?P<person_id>\d+)/create/$',
                view=views.TrusteeCreateView.as_view(),
                name='create'
            ),
        ), namespace="trustee")),
)
