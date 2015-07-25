from django.contrib import admin
from reversion_compare.admin import CompareVersionAdmin

from .models import Gift


class GiftModelAdmin(CompareVersionAdmin):
    class Meta:
        model = Gift


admin.site.register(Gift, GiftModelAdmin)
