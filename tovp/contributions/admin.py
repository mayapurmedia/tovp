from django.contrib import admin
from reversion_compare.admin import CompareVersionAdmin

from .models import Pledge, BulkPayment, Contribution


class PledgeModelAdmin(CompareVersionAdmin):
    class Meta:
        model = Pledge


class BulkPaymentModelAdmin(CompareVersionAdmin):
    class Meta:
        model = BulkPayment


class ContributionModelAdmin(CompareVersionAdmin):
    class Meta:
        model = Contribution


admin.site.register(BulkPayment, BulkPaymentModelAdmin)
admin.site.register(Pledge, PledgeModelAdmin)
admin.site.register(Contribution, ContributionModelAdmin)
