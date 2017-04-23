from haystack import indexes

from ananta.search_indexes import ContentSearchIndexMixin
from contacts.search_indexes import (PersonSearchIndexMixin,
                                     PledgePersonSearchIndexMixin)

from .models import Pledge, FollowUp, Contribution, BulkPayment


class PledgeIndex(ContentSearchIndexMixin, PersonSearchIndexMixin,
                  indexes.SearchIndex, indexes.Indexable):
    content_name = 'Pledge'
    amount = indexes.IntegerField()
    amount_paid = indexes.IntegerField(model_attr='amount_paid')
    currency = indexes.CharField(model_attr='currency', faceted=True)
    source = indexes.MultiValueField(null=True, faceted=True)
    payments_start_date = indexes.DateTimeField(
        model_attr='payments_start_date')
    info = indexes.CharField(model_attr='info')
    interval = indexes.CharField(model_attr='get_interval_display',
                                 faceted=True)
    status = indexes.CharField(model_attr='get_status_display', faceted=True)
    promotion_type = indexes.MultiValueField(null=True, faceted=True)

    next_payment_date = indexes.DateTimeField(model_attr='update_next_payment_date')
    followed_by = indexes.CharField(faceted=True)
    progress = indexes.CharField()

    def prepare_amount(self, obj):
        """ Return amount_paid for zero pledges. """
        if not obj.amount:
            return obj.amount_paid
        return obj.amount

    def prepare_progress(self, obj):
        progress = obj.progress
        if not obj.amount:
            progress = 100
        return "{progress:.2f}%".format(progress=progress)

    def prepare_source(self, obj):
        items = []
        if obj.source:
            items.append(obj.source.name)
            if obj.source.name in ['jps-office', 'namahatta', 'jps-others']:
                items.append('JPS (All combined)')
        return items

    def get_model(self):
        return Pledge

    def prepare_promotion_type(self, obj):
        items = []
        for promotion in obj.assigned_promotions:
            try:
                items.append(promotion._meta.verbose_name.title())
            except:
                items.append('Noname')
        return items

    def prepare_followed_by(self, obj):
        if obj.followed_by:
            return obj.followed_by.display_name
        else:
            return 'Nobody'


class FollowUpIndex(ContentSearchIndexMixin, PledgePersonSearchIndexMixin,
                    indexes.SearchIndex, indexes.Indexable):
    content_name = 'Follow Up'
    status = indexes.CharField(model_attr='get_status_display', faceted=True)
    followed_by = indexes.CharField(faceted=True)
    source = indexes.MultiValueField(null=True, faceted=True)
    amount = indexes.IntegerField(model_attr='pledge__amount')
    currency = indexes.CharField(model_attr='pledge__currency', faceted=True)

    def prepare_followed_by(self, obj):
        if obj.created_by:
            return obj.created_by.display_name

    def prepare_source(self, obj):
        items = []
        # without the next if-clause elasticsearch tries to index pledges w/o a source, throwing fatal errors.
        # TODO: assign some default source to pledges that have none.
        if obj.pledge.source:
            source = obj.pledge.source.name
            if source not in items:
                items.append(source)
                if obj.pledge.source in ['jps-office', 'namahatta', 'jps-others']:
                    items.append('JPS (All combined)')
        for contribution in obj.pledge.contributions.all():
            if contribution.source:
                source = contribution.source.name
                if source not in items:
                    items.append(source)
                    if contribution.source in ['jps-office', 'namahatta', 'jps-others']:
                        items.append('JPS (All combined)')

        return items

    def get_model(self):
        return FollowUp


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
    receipt_type = indexes.CharField(model_attr='get_receipt_type_display',
                                     faceted=True)
    status = indexes.CharField(model_attr='get_status_display', faceted=True)
    book_number = indexes.CharField(model_attr='book_number')
    slip_number = indexes.CharField(model_attr='slip_number')
    overwrite_name = indexes.CharField(model_attr='overwrite_name')
    overwrite_address = indexes.CharField(model_attr='overwrite_address')
    serial_number_clean = indexes.IntegerField()
    serial_number = indexes.CharField()
    has_book = indexes.CharField(faceted=True)
    has_slip = indexes.CharField(faceted=True)
    note = indexes.CharField(model_attr='note')

    foreign_amount = indexes.IntegerField(null=True, model_attr='foreign_amount')
    foreign_currency = indexes.CharField(model_attr='foreign_currency', faceted=True)

    def prepare_source(self, obj):
        items = []
        if obj.source:
            items.append(obj.source.name)
            if obj.source in ['jps-office', 'namahatta', 'jps-others']:
                items.append('JPS (All combined)')
        if getattr(obj, 'pledge', None) and obj.pledge.source:
            source = obj.pledge.source.name
            if source not in items:
                items.append(source)
                if source in ['jps-office', 'namahatta', 'jps-others']:
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

    def prepare_serial_number_clean(self, obj):
        if obj.serial_year and obj.serial_number:
            return int(obj.serial_number)
        return None

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
    promotion_type = indexes.MultiValueField(null=True, faceted=True)
    collector = indexes.MultiValueField(null=True)
    pan_card_number = indexes.CharField()
    address = indexes.CharField()

    def prepare_address(self, obj):
        address = ''
        if obj.overwrite_address:
            address = obj.overwrite_address
        elif obj.pledge.person.pan_card_number:
            address = obj.pledge.person.address
        return address

    def prepare_pan_card_number(self, obj):
        pan_card_number = ''
        if obj.overwrite_pan_card:
            pan_card_number = obj.overwrite_pan_card
        elif obj.pledge.person.pan_card_number:
            pan_card_number = obj.pledge.person.pan_card_number
        return pan_card_number

    def prepare_collector(self, obj):
        items = []
        if obj.collector:
            items.append(obj.collector.pk)
        if getattr(obj, 'bulk_payment', None):
            collector = obj.bulk_payment.person.pk
            if collector not in items:
                items.append(collector)
        return items

    def get_model(self):
        return Contribution

    def prepare_is_external(self, obj):
        if not obj.is_external:
            return 'Mayapur TOVP Receipt'
        return 'External'

    def prepare_promotion_type(self, obj):
        items = []
        for promotion in obj.pledge.assigned_promotions:
            try:
                items.append(promotion._meta.verbose_name.title())
            except:
                items.append('Noname')
        return items


class BulkPaymentIndex(BaseContributionIndexMixin, ContentSearchIndexMixin,
                       PersonSearchIndexMixin, indexes.SearchIndex,
                       indexes.Indexable):
    content_name = 'Bulk Payment'
    receipt_type = indexes.CharField(faceted=True)
    deposited_status = indexes.CharField(faceted=True)

    def prepare_deposited_status(self, obj):
        if obj.payment_method not in ['cashl', 'cashf']:
            return

        deposited = 0
        not_deposited = 0
        # could be done with filter for deposited_status == 'deposited' only
        for contribution in obj.contributions.all():
            if contribution.deposited_status == 'deposited':
                deposited += 1
            else:
                not_deposited += 1
        if not_deposited:
            return 'Not deposited'
        else:
            return 'Deposited'

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
