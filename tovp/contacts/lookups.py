from ajax_select import LookupChannel
from django.core.exceptions import PermissionDenied
from django.utils.html import escape
from django.db.models import Q
from .models import Person


class PersonLookup(LookupChannel):

    model = Person

    def get_query(self, q, request):
        return Person.objects.filter(Q(first_name__icontains=q) | Q(initiated_name__icontains=q) | Q(last_name__istartswith=q))  # .order_by('name')

    def get_result(self, obj):
        u""" result is the simple text that is the completion of what the person typed """
        return obj.mixed_name

    def format_match(self, obj):
        """ (HTML) formatted item for display in the dropdown """
        return self.format_item_display(obj)

    def format_item_display(self, obj):
        """ (HTML) formatted item for displaying item in the selected deck area """
        return u"%s<div></div>" % (escape(obj.mixed_name))

    def check_auth(self, request):
        """Return results only to logged users."""
        if not request.user.is_authenticated():
            raise PermissionDenied
