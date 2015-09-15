from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.SearchView.as_view(), name="index"),
    url(r'^follow-up/$', views.FollowUpView.as_view(), name="follow_up"),
)
