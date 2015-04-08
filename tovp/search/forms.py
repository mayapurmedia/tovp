from django import forms
from django.utils.translation import ugettext as _

from haystack.query import SearchQuerySet


class SearchForm(forms.Form):
    q = forms.CharField(required=False, label=_('Text'),
                        widget=forms.TextInput())  # attrs={'type': 'search'}))
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
    book_number = forms.CharField(required=False, label=_('Book Number'),
                                  widget=forms.TextInput())
    slip_number = forms.CharField(required=False, label=_('Slip Number'),
                                  widget=forms.TextInput())
    transaction_id = forms.CharField(required=False, label=_('Transaction ID'),
                                     widget=forms.TextInput())
    record_id = forms.CharField(required=False, label=_('Record ID'),
                                widget=forms.TextInput())

    def __init__(self, *args, **kwargs):
        self.searchqueryset = kwargs.pop('searchqueryset', None)
        self.load_all = kwargs.pop('load_all', False)

        if self.searchqueryset is None:
            self.searchqueryset = SearchQuerySet()

        super(SearchForm, self).__init__(*args, **kwargs)

    def search(self):
        if not self.is_valid():
            return self.show_all()

        sqs = self.show_all()

        if self.cleaned_data.get('q'):
            # sqs = sqs.auto_query(self.cleaned_data['q'])
            sqs = sqs.filter(text__contains=self.cleaned_data['q'])

        # fields which are filtered with __contains
        contains = [
            'email', 'serial_number',
        ]

        for field_name in contains:
            if self.cleaned_data.get(field_name):
                sqs = sqs.filter(**{'%s__contains' % field_name:
                                    self.cleaned_data[field_name]})

        # fields which are filtered with __startswith
        starts_with = [
            'mixed_name', 'initiated_name', 'first_name', 'middle_name',
            'last_name', 'pan_card_number', 'phone_number',
            'book_number', 'slip_number', 'transaction_id',
            'record_id']

        for field_name in starts_with:
            if self.cleaned_data.get(field_name):
                sqs = sqs.filter(**{'%s__startswith' % field_name:
                                    self.cleaned_data[field_name]})
        return sqs

    def show_all(self):
        return self.searchqueryset.order_by('-modified')
