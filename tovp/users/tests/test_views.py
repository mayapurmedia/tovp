from urllib.parse import quote
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase, Client

from ..models import User


class UserViewsTests(TestCase):
    def setUp(self):
        self.password = 'mypassword'

        self.admin_user = User.objects.create_superuser(
            'admin', 'admin@test.com', 'Administrator', self.password)
        self.user = User.objects.create_user('normal-user', 'user@test.com',
                                             'Normal User', self.password)

    def test_login_logout(self):
        # testing login
        client = Client()
        result = client.login(username='normal-user', password=self.password)
        self.assertEqual(result, True)

        # testing logout
        client.logout()
        self.assertEqual(client.session, {})

    def test_user_redirect_view_not_logged(self):
        client = Client()
        response = client.get(reverse('users:redirect'), follow=True)
        self.assertRedirects(
            response,
            '%s?next=%s' % (reverse('users:login'),
                            quote(reverse('users:redirect'))),
            status_code=302,
            target_status_code=200)

    def test_user_redirect_view_logged_in(self):
        client = Client()
        client.login(username='normal-user', password=self.password)

        response = client.get(reverse('users:redirect'), follow=True)
        self.assertRedirects(
            response,
            reverse('users:detail', kwargs={'username': 'normal-user'}),
            status_code=302,
            target_status_code=200)

    def test_user_update_view_change_fields(self):
        """
        Checks if all fields are saved when changed.
        """
        client = Client()
        client.login(username=self.user.username, password=self.password)

        response = client.post(
            reverse('users:update'),
            {
                'username': 'normal-user-renamed',
                'email': 'newmail@test.com',
                'password1': 'mynewpassword',
                'password2': 'mynewpassword',
            },
            follow=True,
        )

        # Check if view got redirected to user profile
        self.assertRedirects(
            response,
            reverse('users:detail', kwargs={'username': 'normal-user-renamed'}),
            status_code=302,
            target_status_code=200)

        # user got renamed, so there it should not return user with old username
        with self.assertRaises(ObjectDoesNotExist):
            User.objects.get(username='normal-user')

        # load renamed user
        updated_user = User.objects.get(username='normal-user-renamed')

        # Check if new password got saved
        self.assertEqual(updated_user.check_password('mynewpassword'), True)

        # Check if new email got saved
        self.assertEqual(updated_user.email, 'newmail@test.com')

    def test_user_update_view_no_changes(self):
        """
        Checks if fields stay same when we don't change values.
        """
        client = Client()
        client.login(username=self.user.username, password=self.password)

        response = client.post(
            reverse('users:update'),
            {
                'username': 'normal-user',
                'email': 'user@test.com',
            },
            follow=True,
        )

        # Check if view got redirected to user profile
        self.assertRedirects(
            response,
            reverse('users:detail', kwargs={'username': 'normal-user'}),
            status_code=302,
            target_status_code=200)

        # load user
        updated_user = User.objects.get(username='normal-user')

        # Check if email is still same
        self.assertEqual(updated_user.email, 'user@test.com')

        # Check if password is still same
        self.assertEqual(updated_user.check_password('mypassword'), True)

    def test_user_update_view_not_matching_password(self):
        """
        Checks if two different password will raise error.
        """
        client = Client()
        client.login(username=self.user.username, password=self.password)

        response = client.post(
            reverse('users:update'),
            {
                'username': 'normal-user',
                'email': 'user@test.com',
                'password1': 'mynewpassword',
                'password2': 'mynewpassword-not-same',
            },
            follow=True,
        )

        self.assertFormError(response, 'form', 'password2',
                             'Passwords do not match.')

    def test_user_update_view_already_registered_email(self):
        """
        Checks if already registered email by different user will raise error.
        """
        client = Client()
        client.login(username=self.user.username, password=self.password)

        response = client.post(
            reverse('users:update'),
            {
                'username': 'normal-user',
                'email': 'admin@test.com',
            },
            follow=True,
        )

        self.assertFormError(response, 'form', 'email',
                             'This email is already registered.')
