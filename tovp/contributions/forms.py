from django import forms

from datetimewidget.widgets import DateWidget

from .models import Pledge, Contribution

from contacts.models import Person


class PledgeForm(forms.ModelForm):
    person = forms.ModelChoiceField(queryset=Person.objects.all(),
                                    widget=forms.HiddenInput())

    class Meta:
        model = Pledge
        exclude = ('status_changed',)
        widgets = {
            'payments_start_date': DateWidget(
                attrs={},
                options={'startView': 2, 'format': 'yyyy-mm-dd'},
                bootstrap_version=3
            ),
        }


class ContributionForm(forms.ModelForm):
    person = forms.ModelChoiceField(queryset=Person.objects.all(),
                                    widget=forms.HiddenInput())

    def __init__(self, person, *args, **kwargs):
        super(ContributionForm, self).__init__(*args, **kwargs)
        self.fields['pledge'].queryset = Pledge.objects.filter(
            person=person)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['amount'].widget.attrs['readonly'] = True
            self.fields['currency'].widget.attrs['readonly'] = True
            self.fields['receipt_date'].widget.attrs['readonly'] = True
            if instance._serial_year:
                self.fields['is_external'].widget.attrs['readonly'] = True
                self.fields['is_external'].widget.attrs['disabled'] = True
            if instance.status == 'completed':
                self.fields['status'].widget.attrs['readonly'] = True
                self.fields['cleared_on'].widget.attrs['readonly'] = True

    class Meta:
        model = Contribution
        exclude = ('status_changed',)
        widgets = {
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
