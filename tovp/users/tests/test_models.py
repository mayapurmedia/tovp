from django.test import TestCase

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
