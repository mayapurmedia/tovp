from django import forms

from datetimewidget.widgets import DateWidget

from .models import Contribution

from contacts.models import Person


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
