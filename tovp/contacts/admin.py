from django.contrib import admin
from reversion_compare.admin import CompareVersionAdmin

from .models import Person


class PersonModelAdmin(CompareVersionAdmin):
    class Meta:
        model = Person


admin.site.register(Person, PersonModelAdmin)
