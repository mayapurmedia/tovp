from __future__ import unicode_literals

from django.test import TestCase
from django.forms.fields import Field
from django.utils.encoding import force_text

from ..models import User
from ..forms import UserCreationForm, UserChangeForm


class UserCreationFormTest(TestCase):
    def setUp(self):
        self.password = 'mypassword'
        self.admin_user = User.objects.create_superuser(
            'admin', 'admin@test.com', 'Administrator', self.password)
        self.user = User.objects.create_user('normal-user', 'user@test.com',
                                             'Normal User', self.password)

    def test_user_already_exists(self):
        data = {
            'username': 'normal-user',
            'password1': 'test123',
            'password2': 'test123',
        }
        form = UserCreationForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form["username"].errors,
                         [force_text(User._meta.get_field('username').
                                     error_messages['unique'])])

    def test_invalid_data(self):
        data = {
            'username': 'wrong-username!!!',
            'password1': 'test123',
            'password2': 'test123',
        }
        form = UserCreationForm(data)
        self.assertFalse(form.is_valid())
        validator = next(v for v in User._meta.get_field('username').
                         validators if v.code == 'invalid')
        self.assertEqual(form["username"].errors,
                         [force_text(validator.message)])

    def test_password_verification(self):
        # The verification password is incorrect.
        data = {
            'username': 'username',
            'password1': 'test123',
            'password2': 'test',
        }
        form = UserCreationForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form["password2"].errors,
                         [force_text(form.error_messages['password_mismatch'])])

    def test_both_passwords(self):
        # One (or both) passwords weren't given
        data = {'username': 'username'}
        form = UserCreationForm(data)
        required_error = [force_text(Field.default_error_messages['required'])]
        self.assertFalse(form.is_valid())
        self.assertEqual(form['password1'].errors, required_error)
        self.assertEqual(form['password2'].errors, required_error)

        data['password2'] = 'test123'
        form = UserCreationForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form['password1'].errors, required_error)
        self.assertEqual(form['password2'].errors, [])

    def test_success(self):
        data = {
            'username': 'new-user',
            'password1': 'test123',
            'password2': 'test123',
        }
        form = UserCreationForm(data)
        self.assertTrue(form.is_valid())
        u = form.save()
        self.assertEqual(repr(u), '<User: new-user>')


class UserChangeFormTest(TestCase):
    def setUp(self):
        self.password = 'mypassword'
        self.admin_user = User.objects.create_superuser(
            'admin', 'admin@test.com', 'Administrator', self.password)
        self.user = User.objects.create_user('normal-user', 'user@test.com',
                                             'Normal User', self.password)

    def test_username_validity(self):
        user = User.objects.get(username='normal-user')
        data = {'username': 'not valid'}
        form = UserChangeForm(data, instance=user)
        self.assertFalse(form.is_valid())
        validator = next(v for v in User._meta.get_field('username').
                         validators if v.code == 'invalid')
        self.assertEqual(form["username"].errors,
                         [force_text(validator.message)])

    def test_password_verification(self):
        user = User.objects.get(username='normal-user')
        # The verification password is incorrect.
        data = {
            'username': 'nomal-user',
            'password1': 'test123',
            'password2': 'test',
        }
        form = UserChangeForm(data, instance=user)
        self.assertFalse(form.is_valid())
        self.assertEqual(form["password2"].errors,
                         [force_text(form.error_messages['password_mismatch'])])

    def test_both_passwords(self):
        user = User.objects.get(username='normal-user')
        data = {
            'password1': 'test',
            'password2': 'test123',
        }
        form = UserChangeForm(data, instance=user)
        self.assertFalse(form.is_valid())
        self.assertEqual(form["password2"].errors,
                         [force_text(form.error_messages['password_mismatch'])])

    def test_success(self):
        user = User.objects.get(username='normal-user')
        form_for_data = UserChangeForm(instance=user)
        post_data = dict(form_for_data.initial, **{
            'username': 'new-username',
            'password1': 'new-password',
            'password2': 'new-password',
        })

        form = UserChangeForm(instance=user, data=post_data)
        self.assertTrue(form.is_valid())
        u = form.save()
        self.assertEqual(repr(u), '<User: new-username>')
        self.assertEqual(u.check_password('new-password'), True)
