from ajax_select import LookupChannel
from django.utils.html import escape
from django.db.models import Q
from .models import BulkPayment


class BulkPaymentLookup(object):

    def get_query(self, q, request):
        return BulkPayment.objects.filter(Q(pk__startswith=q) | Q(person__first_name__icontains=q) | Q(person__initiated_name__icontains=q) | Q(person__last_name__icontains=q))  # .order_by('name')

    def get_result(self, obj):
        u""" result is the simple text that is the completion of what the person typed """
        return obj.person.mixed_name

    def format_match(self, obj):
        """ (HTML) formatted item for display in the dropdown """
        return self.format_item_display(obj)

    def format_item_display(self, obj):
        """ (HTML) formatted item for displaying item in the selected deck area """
        return u"{name}<div>{amount} {currency}</div><div>{date}</div>". \
            format(name=escape(obj.person.mixed_name), amount=obj.amount,
                   currency=obj.currency, date=obj.receipt_date)
