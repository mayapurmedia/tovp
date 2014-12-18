from django import forms
from .models import User


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
            raise forms.ValidationError('This email is already registered')

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Passwords do not match.')

    def __init__(self, *args, **kwargs):
        return super(UserUpdateForm, self).__init__(*args, **kwargs)
