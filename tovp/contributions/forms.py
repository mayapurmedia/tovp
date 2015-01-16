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
        }
