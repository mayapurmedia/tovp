from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.SearchView.as_view(), name="index"),
    url(r'^follow-up/$', views.FollowUpView.as_view(), name="follow_up"),
]