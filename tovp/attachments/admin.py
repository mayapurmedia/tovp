from django.contrib.contenttypes.admin import GenericStackedInline
from django.contrib import admin
from reversion_compare.admin import CompareVersionAdmin
from .models import Attachment


class AttachmentInlines(GenericStackedInline):
    model = Attachment
    extra = 1


class AttachmentModelAdmin(CompareVersionAdmin):
    class Meta:
        model = Attachment

admin.site.register(Attachment, AttachmentModelAdmin)
