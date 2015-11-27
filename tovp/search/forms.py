from datetime import datetime
from django import forms
from django.utils.translation import ugettext as _

from datetimewidget.widgets import DateWidget
from haystack.query import SearchQuerySet

from contacts.models import Person


class SearchForm(forms.Form):
    q = forms.CharField(required=False, label=_('Search Text'),
                        widget=forms.TextInput())
    # has_releases = forms.BooleanField(label=_("Has Releases"),
    #                                   required=False, initial=True)
    mixed_name = forms.CharField(required=False, label=_('Mixed Name'),
                                 widget=forms.TextInput())
    first_name = forms.CharField(required=False, label=_('First Name'),
                                 widget=forms.TextInput())
    last_name = forms.CharField(required=False, label=_('Last Name'),
                                widget=forms.TextInput())
    initiated_name = forms.CharField(required=False, label=_('Initiated Name'),
                                     widget=forms.TextInput())
    email = forms.CharField(required=False, label=_('Email'),
                            widget=forms.TextInput())
    pan_card_number = forms.CharField(required=False,
                                      label=_('Pan Card Number'),
                                      widget=forms.TextInput())
    serial_number = forms.CharField(required=False, label=_('Serial Number'),
                                    widget=forms.TextInput())
    phone_number = forms.CharField(required=False, label=_('Phone Number'),
                                   widget=forms.TextInput())
    old_database_id = forms.CharField(required=False, label=_('Old Database Id'),
                                      widget=forms.TextInput())
    book_number = forms.CharField(required=False, label=_('Book Number'),
                                  widget=forms.TextInput())
    postcode = forms.CharField(required=False, label=_('Post Code'),
                               widget=forms.TextInput())
    slip_number = forms.CharField(required=False, label=_('Slip Number'),
                                  widget=forms.TextInput())
    transaction_id = forms.CharField(required=False, label=_('Transaction ID'),
                                     widget=forms.TextInput())
    record_id = forms.CharField(required=False, label=_('Record ID'),
                                widget=forms.TextInput())
    collector = forms.ChoiceField(required=False, label='Collector',
                                  choices=())

    DATE_TYPE_CHOICES = (
        (u'receipt_date', _('Receipt Date')),
        (u'cleared_on', _('Cleared On')),
        (u'dated', _('Dated')),
        (u'created', _('Created on')),
        (u'modified', _('Last modified on')),
    )

    date_type = forms.ChoiceField(required=False, label='Date Type',
                                  choices=DATE_TYPE_CHOICES)
    date_from = forms.CharField(
        required=False, label=_('Date From'),
        widget=DateWidget(attrs={'id': "date-from"},
                          usel10n=True, bootstrap_version=3))
    date_to = forms.CharField(
        required=False, label=_('Date To'),
        widget=DateWidget(attrs={'id': "date-to"},
                          usel10n=True, bootstrap_version=3))

    ORDER_CHOICES = (
        (u'modified', _('Modified')),
        (u'created', _('Created')),
        (u'cleared_on', _('Cleared On')),
        (u'receipt_date', _('Receipt Date')),
        (u'serial_number_clean', _('Serial Number')),
    )

    order = forms.ChoiceField(required=False, label='Order by',
                              choices=ORDER_CHOICES)
    ORDER_TYPE_CHOICES = (
        (u'asc', _('Ascending')),
        (u'desc', _('Descending')),
    )

    order_type = forms.ChoiceField(required=False, label='Order type',
                                   choices=ORDER_TYPE_CHOICES)

    serial_clean_from = forms.CharField(required=False, label=_('Serial From'),
                                        widget=forms.TextInput())
    serial_clean_to = forms.CharField(required=False, label=_('Serial To'),
                                      widget=forms.TextInput())

    def __init__(self, collector_pk=None, *args, **kwargs):
        self.collector_pk = None
        self.searchqueryset = kwargs.pop('searchqueryset', None)
        self.load_all = kwargs.pop('load_all', False)

        if self.searchqueryset is None:
            self.searchqueryset = SearchQuerySet()

        super(SearchForm, self).__init__(*args, **kwargs)
        if collector_pk:
            try:
                collector = Person.objects.filter(pk=collector_pk)[0]
                self.fields['collector'].choices = ((collector.pk, collector.mixed_name),)
                self.collector_pk = collector_pk
            except:
                pass

    def search(self):
        if not self.is_valid():
            return self.show_all()

        if self.cleaned_data.get('order_type') == 'desc':
            order_type = '-'
        else:
            order_type = ''

        if self.cleaned_data.get('order'):
            sqs = self.searchqueryset.order_by('%s%s' % (order_type, self.cleaned_data.get('order')))
        else:
            sqs = self.searchqueryset.order_by('%smodified' % order_type)

        if self.cleaned_data.get('q'):
            # sqs = sqs.auto_query(self.cleaned_data['q'])
            sqs = sqs.filter(text__contains=self.cleaned_data['q'])

        # fields which are filtered with __contains
        contains = [
            'email', 'serial_number', 'phone_number', 'old_database_id',
        ]

        for field_name in contains:
            if self.cleaned_data.get(field_name):
                sqs = sqs.filter(**{'%s__contains' % field_name:
                                    self.cleaned_data[field_name]})

        # fields which are filtered with __startswith
        starts_with = [
            'mixed_name', 'initiated_name', 'first_name', 'middle_name',
            'last_name', 'pan_card_number', 'record_id', 'postcode',
            'book_number', 'slip_number', 'transaction_id']

        for field_name in starts_with:
            if self.cleaned_data.get(field_name):
                sqs = sqs.filter(**{'%s__startswith' % field_name:
                                    self.cleaned_data[field_name]})

        date_type = self.cleaned_data.get('date_type')
        field_name = 'date_from'
        if self.cleaned_data.get(field_name):
            filter_date = datetime.strptime(
                self.cleaned_data.get(field_name), '%Y-%m-%d')
            sqs = sqs.filter(**{'%s__gte' % date_type: filter_date})

        field_name = 'date_to'
        if self.cleaned_data.get(field_name):
            filter_date = datetime.strptime(
                self.cleaned_data.get(field_name), '%Y-%m-%d')
            sqs = sqs.filter(**{'%s__lte' % date_type: filter_date})

        field_name = 'collector'
        if self.collector_pk:
            sqs = sqs.filter(**{'%s__startswith' % field_name:
                                self.collector_pk})

        field_name = 'serial_clean_from'
        if self.cleaned_data.get(field_name):
            sqs = sqs.filter(**{'%s__gte' % 'serial_number_clean': self.cleaned_data.get(field_name)})

        field_name = 'serial_clean_to'
        if self.cleaned_data.get(field_name):
            sqs = sqs.filter(**{'%s__lte' % 'serial_number_clean': self.cleaned_data.get(field_name)})

        return sqs

    def show_all(self):
        return self.searchqueryset.order_by('-modified')


class FollowUpForm(SearchForm):
    def show_all(self):
        self.searchqueryset = SearchQuerySet()
        return self.searchqueryset. \
            filter(content_type='Pledge'). \
            filter(next_payment_date__lte=datetime.now()). \
            exclude(status='Completed'). \
            order_by('next_payment_date')

    def search(self):
        return self.show_all()
