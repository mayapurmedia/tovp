# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
# from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from ajax_select import urls as ajax_select_urls

admin.autodiscover()

urlpatterns = [
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^users/', include("users.urls", namespace="users")),

    url(r'^', include("donate.urls", namespace="donate")),
    url(r'^donor-list', include("donor_list.urls", namespace="donor_list")),

    url(r'^database/', include("search.urls", namespace="search")),
    url(r'^database/contacts/', include("contacts.urls", namespace="contacts")),
    url(r'^database/promotions/', include("promotions.urls",
                                          namespace="promotions")),
    url(r'^database/gifts/', include("gifts.urls", namespace="gifts")),
    url(r'^database/contributions/', include("contributions.urls",
                                             namespace="contributions")),

    url(r'^hijack/', include('hijack.urls')),
    url(r'^attachments/', include('attachments.urls')),
    url(r'^ajax_select/lookups/', include(ajax_select_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
