from haystack import indexes

from ananta.search_indexes import ContentSearchIndexMixin
from contacts.search_indexes import (PersonSearchIndexMixin,
                                     PledgePersonSearchIndexMixin)

from .models import Pledge, Contribution, BulkPayment


class PledgeIndex(ContentSearchIndexMixin, PersonSearchIndexMixin,
                  indexes.SearchIndex, indexes.Indexable):
    content_name = 'Pledge'
    amount = indexes.IntegerField(model_attr='amount')
    amount_paid = indexes.IntegerField(model_attr='amount_paid')
    currency = indexes.CharField(model_attr='currency', faceted=True)
    source = indexes.MultiValueField(null=True, faceted=True)
    payments_start_date = indexes.DateTimeField(
        model_attr='payments_start_date')
    info = indexes.CharField(model_attr='info')
    interval = indexes.CharField(model_attr='get_interval_display',
                                 faceted=True)
    status = indexes.CharField(model_attr='get_status_display', faceted=True)
    promotion_type = indexes.CharField(faceted=True)
    # next_payment_date =

    def prepare_source(self, obj):
        items = []
        if obj.source:
            items.append(obj.get_source_display())
            if obj.source in ['jps-office', 'namahatta', 'jps-others']:
                items.append('JPS (All combined)')
        return items

    def get_model(self):
        return Pledge

    def prepare_promotion_type(self, obj):
        for promotion in obj.assigned_promotions():
            try:
                return promotion._meta.verbose_name.title()
                # return self.promotion_type
            except:
                return 'Noname'


class BaseContributionIndexMixin(indexes.SearchIndex):
    amount = indexes.IntegerField(model_attr='amount')
    currency = indexes.CharField(model_attr='currency', faceted=True)
    payment_method = indexes.CharField(model_attr='get_payment_method_display',
                                       faceted=True)
    transaction_id = indexes.CharField(model_attr='transaction_id')
    bank = indexes.CharField(model_attr='bank', faceted=True)
    receipt_date = indexes.DateTimeField()
    dated = indexes.DateTimeField()
    cleared_on = indexes.DateTimeField()
    source = indexes.MultiValueField(null=True, faceted=True)
    status = indexes.CharField(model_attr='get_status_display', faceted=True)
    book_number = indexes.CharField(model_attr='book_number')
    slip_number = indexes.CharField(model_attr='slip_number')
    overwrite_name = indexes.CharField(model_attr='overwrite_name')
    overwrite_address = indexes.CharField(model_attr='overwrite_address')
    serial_number = indexes.CharField()
    has_book = indexes.CharField(faceted=True)
    has_slip = indexes.CharField(faceted=True)
    note = indexes.CharField(model_attr='note')

    def prepare_source(self, obj):
        items = []
        if obj.source:
            items.append(obj.get_source_display())
            if obj.source in ['jps-office', 'namahatta', 'jps-others']:
                items.append('JPS (All combined)')
        if getattr(obj, 'pledge', None) and obj.pledge.source:
            source = obj.pledge.get_source_display()
            if source not in items:
                items.append(source)
                if obj.source in ['jps-office', 'namahatta', 'jps-others']:
                    items.append('JPS (All combined)')
        return items

    def prepare_receipt_date(self, obj):
        if obj.receipt_date:
            return obj.receipt_date

    def prepare_dated(self, obj):
        if obj.dated:
            return obj.dated

    def prepare_has_book(self, obj):
        if not obj.book_number:
            return 'Missing'
        return 'Yes'

    def prepare_has_slip(self, obj):
        if not obj.slip_number:
            return 'Missing'
        return 'Yes'

    def prepare_cleared_on(self, obj):
        if obj.cleared_on:
            return obj.cleared_on

    def prepare_serial_number(self, obj):
        if obj.get_serial_number():
            return obj.get_serial_number()


class ContributionIndex(BaseContributionIndexMixin,
                        ContentSearchIndexMixin, PledgePersonSearchIndexMixin,
                        indexes.SearchIndex, indexes.Indexable):
    content_name = 'Contribution'
    deposited_status = indexes.CharField(
        model_attr='get_deposited_status_display', faceted=True)
    is_external = indexes.CharField(faceted=True)
    promotion_type = indexes.CharField(faceted=True)

    def get_model(self):
        return Contribution

    def prepare_is_external(self, obj):
        if not obj.is_external:
            return 'Mayapur TOVP Receipt'
        return 'External'

    def prepare_promotion_type(self, obj):
        for promotion in obj.pledge.assigned_promotions():
            try:
                return promotion._meta.verbose_name.title()
                # return self.promotion_type
            except:
                return 'Noname'


class BulkPaymentIndex(BaseContributionIndexMixin, ContentSearchIndexMixin,
                       PersonSearchIndexMixin, indexes.SearchIndex,
                       indexes.Indexable):
    content_name = 'Bulk Payment'
    receipt_type = indexes.CharField(faceted=True)

    def get_model(self):
        return BulkPayment

    def prepare_dated(self, obj):
        if obj.dated:
            return obj.dated

    def prepare_has_book(self, obj):
        if not obj.book_number:
            return 'Missing'
        return 'Yes'

    def prepare_has_slip(self, obj):
        if not obj.slip_number:
            return 'Missing'
        return 'Yes'

    def prepare_cleared_on(self, obj):
        if obj.cleared_on:
            return obj.cleared_on

    def prepare_serial_number(self, obj):
        if obj.get_serial_number():
            return obj.get_serial_number()
