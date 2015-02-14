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
    pan_card_number = forms.CharField(required=False, label=_('Pan Card Number'),
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

        if self.cleaned_data.get('mixed_name'):
            sqs = sqs.filter(mixed_name__startswith=self.cleaned_data['mixed_name'])

        if self.cleaned_data.get('initiated_name'):
            # sqs =
            # self.searchqueryset.filter(initiated_name__startswith=self.cleaned_data['initiated_name'])
            sqs = sqs.filter(initiated_name__startswith=self.cleaned_data['initiated_name'])

        if self.cleaned_data.get('first_name'):
            sqs = sqs.filter(first_name__startswith=self.cleaned_data['first_name'])

        if self.cleaned_data.get('last_name'):
            sqs = sqs.filter(last_name__startswith=self.cleaned_data['last_name'])

        if self.cleaned_data.get('email'):
            sqs = sqs.filter(email__startswith=self.cleaned_data['email'])

        if self.cleaned_data.get('pan_card_number'):
            sqs = sqs.filter(pan_card_number__startswith=self.cleaned_data['pan_card_number'])

        if self.cleaned_data.get('book_number'):
            sqs = sqs.filter(book_number__startswith=self.cleaned_data['book_number'])

        if self.cleaned_data.get('slip_number'):
            sqs = sqs.filter(slip_number__startswith=self.cleaned_data['slip_number'])

        if self.cleaned_data.get('transaction_id'):
            sqs = sqs.filter(transaction_id__startswith=self.cleaned_data['transaction_id'])

        if self.cleaned_data.get('record_id'):
            # in case when somebody use id in form TOVPxxx we remove 'tovp' part
            record_id = self.cleaned_data.get('record_id').lower().replace('tovp', '')
            sqs = sqs.filter(record_id__startswith=record_id)

        # if self.cleaned_data.get('pan_card_number'):
        #     sqs = sqs.filter(pan_card_number__startswith=self.cleaned_data['pan_card_number'])

        # if self.cleaned_data.get('pan_card_number'):
        #     sqs = sqs.filter(pan_card_number__startswith=self.cleaned_data['pan_card_number'])

        # if self.cleaned_data.get('pan_card_number'):
        #     sqs = sqs.filter(pan_card_number__startswith=self.cleaned_data['pan_card_number'])

        # if self.cleaned_data.get('pan_card_number'):
        #     sqs = sqs.filter(pan_card_number__startswith=self.cleaned_data['pan_card_number'])

        # if self.cleaned_data.get('pan_card_number'):
        #     sqs = sqs.filter(pan_card_number__startswith=self.cleaned_data['pan_card_number'])

        return sqs

    def show_all(self):
        return self.searchqueryset  # .order_by('-created_on')
