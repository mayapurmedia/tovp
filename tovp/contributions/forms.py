from django import forms
from django.utils.safestring import mark_safe
from django.forms import TextInput

from datetimewidget.widgets import DateWidget

from ajax_select import make_ajax_field

from .models import Pledge, Contribution, BulkPayment

from contacts.models import Person


class PledgeForm(forms.ModelForm):
    person = forms.ModelChoiceField(queryset=Person.objects.all(),
                                    widget=forms.HiddenInput())

    class Meta:
        model = Pledge
        exclude = ('status_changed',)
        widgets = {
            'amount': TextInput(attrs={'type': 'text'}),
            'payments_start_date': DateWidget(
                attrs={},
                options={'startView': 2, 'format': 'yyyy-mm-dd'},
                bootstrap_version=3
            ),
        }


class NoInput(forms.Widget):
    def render(self, name, value, attrs=None):
        return mark_safe(value)


class StaticField(forms.Field):
    widget = NoInput

    def clean(self, value):
        return


class ContributionForm(forms.ModelForm):
    collector = make_ajax_field(Contribution, 'collector', 'person', help_text=None)
    bulk_payment = make_ajax_field(Contribution, 'bulk_payment', 'bulk_payment', help_text=None)

    def __init__(self, person, *args, **kwargs):
        super(ContributionForm, self).__init__(*args, **kwargs)
        self.fields['pledge'].queryset = Pledge.objects.filter(
            person=person)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk and instance.serial_number:
            self.fields['amount'] = StaticField()
            self.fields['currency'] = StaticField()
            self.fields['receipt_date'] = StaticField()
            self.fields['is_external'] = StaticField()
            if instance.status == 'completed':
                self.fields['status'] = StaticField()
                self.fields['cleared_on'] = StaticField()
                self.fields['payment_method'] = StaticField()

    def clean(self):
        for name, field in self.fields.items():
            if isinstance(field, StaticField):
                self.cleaned_data.update({name: self.initial[name]})

        return self.cleaned_data

    class Meta:
        model = Contribution
        exclude = ('status_changed',)
        widgets = {
            'amount': TextInput(attrs={'type': 'text'}),
            'dated': DateWidget(
                attrs={},
                options={
                    'startView': 2,
                    'format': 'yyyy-mm-dd',
                },
                bootstrap_version=3
            ),
            'receipt_date': DateWidget(
                attrs={},
                options={
                    'startView': 2,
                    'format': 'yyyy-mm-dd',
                },
                bootstrap_version=3
            ),
            'cleared_on': DateWidget(
                attrs={},
                options={
                    'startView': 2,
                    'format': 'yyyy-mm-dd',
                },
                bootstrap_version=3
            ),
        }


class BulkPaymentForm(forms.ModelForm):
    person = forms.ModelChoiceField(queryset=Person.objects.all(),
                                    widget=forms.HiddenInput())

    def __init__(self, person, *args, **kwargs):
        super(BulkPaymentForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk and instance.serial_number:
            self.fields['amount'] = StaticField()
            self.fields['currency'] = StaticField()
            self.fields['receipt_date'] = StaticField()
            if instance.status == 'completed':
                self.fields['status'] = StaticField()
                self.fields['cleared_on'] = StaticField()
                self.fields['payment_method'] = StaticField()

    def clean(self):
        for name, field in self.fields.items():
            if isinstance(field, StaticField):
                self.cleaned_data.update({name: self.initial[name]})

        return self.cleaned_data

    class Meta:
        model = BulkPayment
        exclude = ('status_changed',)
        widgets = {
            'amount': TextInput(attrs={'type': 'text'}),
            'dated': DateWidget(
                attrs={},
                options={
                    'startView': 2,
                    'format': 'yyyy-mm-dd',
                },
                bootstrap_version=3
            ),
            'receipt_date': DateWidget(
                attrs={},
                options={
                    'startView': 2,
                    'format': 'yyyy-mm-dd',
                },
                bootstrap_version=3
            ),
            'cleared_on': DateWidget(
                attrs={},
                options={
                    'startView': 2,
                    'format': 'yyyy-mm-dd',
                },
                bootstrap_version=3
            ),
        }
