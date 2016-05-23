from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^add-for/(?P<app_label>[\w\-]+)/(?P<model_name>[\w\-]+)/(?P<pk>\d+)/$',
        views.add_attachment,
        name="add_attachment"),
    url(
        r'^delete/(?P<attachment_pk>\d+)/$',
        views.delete_attachment,
        name="delete_attachment"),
]
