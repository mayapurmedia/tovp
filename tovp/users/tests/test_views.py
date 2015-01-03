from urllib.parse import quote
from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from ..models import User


class UserModelTests(TestCase):
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
