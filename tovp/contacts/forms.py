from django import forms

from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ()
        widgets = {
            'address': forms.Textarea(attrs={'rows': 2}),
        }
