from django.contrib import admin
from reversion_compare.admin import CompareVersionAdmin

from .models import Pledge, Contribution


class PledgeModelAdmin(CompareVersionAdmin):
    class Meta:
        model = Pledge


class ContributionModelAdmin(CompareVersionAdmin):
    class Meta:
        model = Contribution


admin.site.register(Pledge, PledgeModelAdmin)
admin.site.register(Contribution, ContributionModelAdmin)
