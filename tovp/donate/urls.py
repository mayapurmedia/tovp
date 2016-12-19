from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.DonateView.as_view(), name="donate"),
    url(r'^donate/save-form/(?P<promotion_slug>[-\w]+)/(?P<region>[-\w]+)/$', views.SaveForm.as_view(), name="save_form"),
    url(r'^donate/(?P<promotion_slug>[-\w]+)/$', views.SelectRegionView.as_view(), name="select_region"),
    url(r'^donate/radha-madhava-brick/(?P<region>[-\w]+)/$', views.DonateRadhaMadhavaBrickView.as_view(), name="radha_madhava_brick"),
    url(r'^donate/nrsimha-tile/(?P<region>[-\w]+)/$', views.DonateNrsimhaTileView.as_view(), name="nrsimha_tile"),
    url(r'^donate/general-donation/(?P<region>[-\w]+)/$', views.DonateNrsimhaTileView.as_view(), name="general_donation"),
    url(r'^donate/golden-brick/(?P<region>[-\w]+)/$', views.DonateGoldenBrickView.as_view(), name="golden_brick"),

]
