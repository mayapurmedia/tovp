from django import forms

from contacts.models import Person

from .models import Gift, GiftGiven


class GiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        exclude = ('status_changed',)


class GiftGivenForm(forms.ModelForm):
    person = forms.ModelChoiceField(queryset=Person.objects.all(),
                                    widget=forms.HiddenInput())

    class Meta:
        model = GiftGiven
        exclude = ('status_changed',)
