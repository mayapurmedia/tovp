from haystack import indexes

from ananta.search_indexes import ContentSearchIndexMixin
from contacts.search_indexes import PersonSearchIndexMixin

from .models import Pledge, Contribution


class PledgeIndex(ContentSearchIndexMixin, PersonSearchIndexMixin,
                  indexes.SearchIndex, indexes.Indexable):
    content_name = 'Pledge'
    text = indexes.CharField(document=True, use_template=True)
    amount = indexes.IntegerField(model_attr='amount')
    amount_paid = indexes.IntegerField(model_attr='amount_paid')
    currency = indexes.CharField(model_attr='currency', faceted=True)
    payments_start_date = indexes.DateTimeField(
        model_attr='payments_start_date')
    info = indexes.CharField(model_attr='info')
    interval = indexes.CharField(model_attr='get_interval_display',
                                 faceted=True)
    status = indexes.CharField(model_attr='get_status_display', faceted=True)
    # next_payment_date =

    def get_model(self):
        return Pledge


class ContributionIndex(ContentSearchIndexMixin, PersonSearchIndexMixin,
                        indexes.SearchIndex, indexes.Indexable):
    content_name = 'Contribution'
    text = indexes.CharField(document=True, use_template=True)
    amount = indexes.IntegerField(model_attr='amount')
    currency = indexes.CharField(model_attr='currency', faceted=True)
    payment_method = indexes.CharField(model_attr='get_payment_method_display',
                                       faceted=True)
    transaction_id = indexes.CharField(model_attr='transaction_id')
    bank = indexes.CharField(model_attr='bank', faceted=True)
    dated = indexes.DateTimeField()
    cleared_on = indexes.DateTimeField()
    status = indexes.CharField(model_attr='get_status_display', faceted=True)
    book_number = indexes.CharField(model_attr='book_number')
    slip_number = indexes.CharField(model_attr='slip_number')
    overwrite_name = indexes.CharField(model_attr='overwrite_name')
    overwrite_address = indexes.CharField(model_attr='overwrite_address')
    serial_number = indexes.CharField()
    has_book = indexes.CharField(faceted=True)
    has_slip = indexes.CharField(faceted=True)
    created_by = indexes.CharField(faceted=True)
    modified_by = indexes.CharField(faceted=True)

    def get_model(self):
        return Contribution

    def prepare_created_by(self, obj):
        if obj.created_by:
            return obj.created_by.display_name

    def prepare_modified_by(self, obj):
        if obj.modified_by:
            return obj.modified_by.display_name

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
