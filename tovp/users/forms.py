from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _

from .models import User


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        # exclude = ['']
        fields = ("username",)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }

    password = ReadOnlyPasswordHashField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = '__all__'

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserChangeForm, self).save(commit=False)
        if self.cleaned_data["password1"]:
            user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Your Email')
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        required=False,
    )
    password2 = forms.CharField(
        label='Password (Again)',
        widget=forms.PasswordInput(),
        required=False,
        help_text='Please write password again.',
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if email == self.instance.email:
            return email
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        else:
            raise forms.ValidationError('This email is already registered.')

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Passwords do not match.')

    def __init__(self, *args, **kwargs):
        return super(UserUpdateForm, self).__init__(*args, **kwargs)
