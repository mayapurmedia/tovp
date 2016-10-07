from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.DonateView.as_view(), name="donate"),
    url(r'^donate/$', views.DonateGeneralView.as_view(), name="general_donation"),
    url(r'^donate/nrsimha-tile/$', views.DonateNrsimhaTileView.as_view(), name="nrsimha_tile"),
    url(r'^donate/golden-brick/$', views.DonateGoldenBrickView.as_view(), name="golden_brick"),
]
