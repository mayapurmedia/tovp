from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.DonateView.as_view(), name="donate"),
]
