from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

from ..models import User


class UserModelTests(TestCase):
    def setUp(self):
        self.password = 'mypassword'
        self.admin_user = User.objects.create_superuser(
            'admin', 'admin@test.com', 'Administrator', self.password)
        self.user = User.objects.create_user('user', 'user@test.com',
                                             'Normal User', self.password)

    def test_create_superuser(self):
        self.assertEqual(self.admin_user.is_superuser, True)
        self.assertEqual(self.admin_user.is_staff, True)

    def test_create_user(self):
        self.assertEqual(self.user.is_superuser, False)
        self.assertEqual(self.user.is_staff, False)

    def test_create_user_empty_username(self):
        with self.assertRaises(ValueError):
            User.objects.create_user('', 'user@test.com', None, self.password)

    def test_get_name(self):
        user = User.objects.create_user('user1', 'user1@test.com', None,
                                        self.password)
        self.assertEqual(user.get_name(), 'user1')
        user.display_name = 'Prahlad Nrsimha Das'
        self.assertEqual(user.get_name(), 'Prahlad Nrsimha Das')
        self.assertEqual(user.get_name(), user.get_full_name())
        self.assertEqual(user.get_name(), user.get_short_name())

    def test_get_link(self):
        from jinja2 import Markup
        self.assertEqual(self.user.get_link(),
                         Markup('<a href="/users/user/">Normal User</a>'))

        self.assertEqual(
            self.user.get_link(css_class='test'),
            Markup('<a class="test" href="/users/user/">Normal User</a>'))

    def test_get_absolute_url_not_logged(self):
        client = Client()

        # for not logged in user there should be redirect
        response = client.get(self.user.get_absolute_url())
        self.assertEqual(response.status_code, 302)

        # not logged users should be redirected to login page first
        self.assertRedirects(
            response,
            '%s?next=%s' % (reverse('users:login'),
                            reverse('users:detail', args=['user'])),
            status_code=302,
            target_status_code=200)

    def test_get_absolute_url_logged_in(self):
        client = Client()
        client.login(username='user', password=self.password)
        response = client.get(self.user.get_absolute_url())
        self.assertEqual(response.status_code, 200)
