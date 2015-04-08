from django import forms
from django.forms import TextInput

from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ()
        widgets = {
            'address': forms.Textarea(attrs={'rows': 2}),
            'old_database_id': TextInput(attrs={'type': 'text'}),
        }
