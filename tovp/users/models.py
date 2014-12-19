from django.db import models
from django.db.models import permalink
from django.utils import timezone
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from jinja2 import Markup, escape


class UserManager(BaseUserManager):
    def _create_user(self, username, email, display_name, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, display_name=display_name,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, display_name=None, password=None, **extra_fields):
        return self._create_user(username, email, display_name, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, email=None, display_name=None, password=None, **extra_fields):
        return self._create_user(username, email, display_name, password, True, True,
                                 **extra_fields)


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'display_name']

    username = models.CharField(
        'username', max_length=60, unique=True,
        help_text='Required. 30 characters or fewer. Letters, digits and '
                  '@/./+/-/_ only.',
        validators=[
            validators.RegexValidator(r'^[\w.@+-]+$', 'Enter a valid username.', 'invalid')
        ])
    email = models.EmailField(blank=True)
    display_name = models.CharField(max_length=200)

    is_active = models.BooleanField(
        'active', default=True,
        help_text='Designates whether this user should be treated as active. '
                  'Unselect this instead of deleting accounts.')

    is_staff = models.BooleanField('staff status', default=False, help_text='Designates whether the user can log into this admin site.')

    is_admin = models.BooleanField(default=False)

    date_joined = models.DateTimeField('date joined', default=timezone.now)

    about = models.TextField(blank=True)

    objects = UserManager()

    def get_name(self):
        if self.display_name:
            return self.display_name
        else:
            return self.user.username

    def get_link(self, css_class=None):
        if css_class:
            return Markup('<a class="%s" href="%s">%s</a>' % (css_class, self.get_absolute_url(), escape(self.display_name)))
        else:
            return Markup('<a href="%s">%s</a>' % (self.get_absolute_url(), escape(self.display_name)))

    @permalink
    def get_absolute_url(self):
        return ('users:detail', None, {'username': self.username})

    def get_full_name(self):
        return self.display_name

    def get_short_name(self):
        return self.display_name

    def __unicode__(self):
        return "%s's profile" % self.display_name
