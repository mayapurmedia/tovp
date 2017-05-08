# -*- coding: utf-8 -*-
"""
Django settings for TOVP project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import join, dirname

from django.core.exceptions import ImproperlyConfigured

import dj_database_url
import django_cache_url
from collections import OrderedDict

BASE_DIR = dirname(dirname(__file__))

# TODO: this should be moved to postactivate too:
BASE_URL = 'https://tovp-donations.org'


def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)


# APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
     'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    # 'django.contrib.humanize',

    # Admin
    'django.contrib.admin',
)

THIRD_PARTY_APPS = (
    'jinja_paginator',
    'datetimewidget',
    'reversion',
    'reversion_compare',
    'haystack',
    'compat',
    'hijack',
    # 'django_extensions',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'ananta',
    'users',  # custom users app
    'contacts',
    'contributions',
    'promotions',
    'gifts',
    'search',
    'theme',
    'attachments',
    'donate',
    'donor_list',
    # Your stuff: custom apps go here
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
# END APP CONFIGURATION

# Flat theme needs to be loaded before admin
INSTALLED_APPS = ('flat',) + INSTALLED_APPS

# MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES = (
    # Make sure djangosecure.middleware.SecurityMiddleware is listed first
    'djangosecure.middleware.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'audit_log.middleware.UserLoggingMiddleware',
    'reversion.middleware.RevisionMiddleware',
)
# END MIDDLEWARE CONFIGURATION

# # MIGRATIONS CONFIGURATION
MIGRATION_MODULES = {
    'sites': 'contrib.sites.migrations'
}
# # END MIGRATIONS CONFIGURATION

# DEBUG
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = bool(os.environ.get('DEBUG', False))

# SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
#       In production, this is changed to a values.SecretValue() setting
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
# END SECRET CONFIGURATION

# FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    join(BASE_DIR, 'fixtures'),
)
# END FIXTURE CONFIGURATION

# EMAIL CONFIGURATION
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')

# collecting SMTP server var's from OS env. (postactivate):
def get_smtp_vars():
    try:
        smtp_vars = os.environ.get('DJANGO_SMTP_VARS')
        smtp_vars = smtp_vars.split( '|' )
        return smtp_vars
    except:
        smtp_vars = ''
        return smtp_vars

smtp_vars = get_smtp_vars()

if len(smtp_vars) == 6:
    EMAIL_HOST = smtp_vars[0]
    EMAIL_HOST_USER = smtp_vars[1]
    EMAIL_HOST_PASSWORD = smtp_vars[2]
    EMAIL_PORT = smtp_vars[3]
    SERVER_EMAIL = smtp_vars[4]
    DEFAULT_FROM_EMAIL = smtp_vars[5]

    EMAIL_USE_SSL = True

# END EMAIL CONFIGURATION

# MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    # removed on his request:
    #("""Prahlad Nrsimha Das (Petr Vacha) - Mayapur Media""", 'pnd@mayapurmedia.com'),
    ("""phanisvara das""", 'phani00@gmail.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# END MANAGER CONFIGURATION

# DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost/tovp')
}

# END DATABASE CONFIGURATION

# CACHING
# Do this here because thanks to django-pylibmc-sasl and pylibmc
# memcacheify (used on heroku) is painful to install on windows.
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': ''
#     }
# }
CACHES = {
    'default': django_cache_url.config()
}
# END CACHING

# GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'Asia/Kolkata'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id

# doesn't seem to do much at present, but should probably go to postactivate as well.
# changed to '2' after adding the new BASE_URL to ~/admin/sites
SITE_ID = 2

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = None
# END GENERAL CONFIGURATION

# TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
_TEMPLATE_CONTEXT_PROCESSORS = (
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    # 'django.contrib.auth.context_processors.auth',
    # 'django.core.context_processors.debug',
    # 'django.core.context_processors.i18n',
    # 'django.core.context_processors.media',
    # 'django.core.context_processors.static',
    # 'django.core.context_processors.tz',
    # 'django.contrib.messages.context_processors.messages',
    # 'django.core.context_processors.request',
    'core.context_processors.variables',
    # # Your stuff: custom template context processers go here
)

# STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
# STATIC_ROOT = join(os.path.dirname(BASE_DIR), 'staticfiles')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = os.environ.get('DJANGO_STATIC_URL', '/static/')
STATIC_ROOT = os.environ.get('DJANGO_STATIC_ROOT', '')

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    # join(BASE_DIR, 'static'),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
# END STATIC FILE CONFIGURATION

# MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = os.environ.get('DJANGO_MEDIA_ROOT', join(BASE_DIR, 'media'))
MEDIA_URL = os.environ.get('DJANGO_MEDIA_URL', '/media/')
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
# END MEDIA CONFIGURATION

# URL Configuration
ROOT_URLCONF = 'tovp.urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'tovp.wsgi.application'
# End URL Configuration

# # AUTHENTICATION CONFIGURATION
AUTHENTICATION_BACKENDS = (
    "users.backends.CaseInsensitiveModelBackend",
    "django.contrib.auth.backends.ModelBackend",
)

# # Custom user app defaults
# # Select the correct user model
AUTH_USER_MODEL = "users.User"
LOGIN_REDIRECT_URL = "users:redirect"
LOGIN_URL = "users:login"
# # END Custom user app defaults

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        "DIRS": ['jinja2'],
        # 'DIRS': [
        #     os.path.join(PROJECT_DIR, 'jinja2'),
        # ],
        'APP_DIRS': True,
        'OPTIONS': {
            'extensions': [
                'ananta.jinja2tags.core',
                # 'ananta.jinja2tags.pagination',
                'promotions.jinja2tags.core',
                'attachments.jinja2tags.core',
                'jinja_paginator.jinja2tags.core',
            ],
            'environment': 'ananta.jinja2.environment',
            # 'core.context_processors.variables',
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": ['templates'],
        # 'DIRS': [
        #     os.path.join(PROJECT_DIR, 'templates'),
        # ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
# END LOGGING CONFIGURATION

ABSOLUTE_DOMAIN = '//tovp-donations.org'

# Your common stuff: Below this line define 3rd party library settings
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.'
        'ElasticsearchSearchEngine',
        'URL': os.environ.get('ELASTICSEARCH_SERVER', 'http://localhost:9200/'),
        'INDEX_NAME': os.environ['ELASTICSEARCH_INDEX_NAME'],
    },
}
HAYSTACK_SIGNAL_PROCESSOR = 'search.signals.RelatedRealtimeSignalProcessor'
HAYSTACK_DEFAULT_OPERATOR = 'AND'

HIJACK_DISPLAY_ADMIN_BUTTON = False
HIJACK_LOGIN_REDIRECT_URL = "/"
HIJACK_LOGOUT_REDIRECT_URL = '/admin/auth/user/'

AJAX_LOOKUP_CHANNELS = {
    'person': ('contacts.lookups', 'PersonLookup'),
    'bulk_payment': ('contributions.lookups', 'BulkPaymentLookup'),
}

ENABLED_CURRENCIES = OrderedDict((
    ('INR', {'word': 'rupees',
             'symbol': '₹ (INR)'}),
    ('USD', {'word': 'american dollars',
             'symbol': '$ (USD)'}),
    ('EUR', {'word': 'euro',
             'symbol': '€ (EUR)'}),
    ('GBP', {'word': 'british pounds',
             'symbol': '£ (GBP)'}),
    ('CAD', {'word': 'canadian dollars',
             'symbol': 'C$ (CAD)'}),
    ('RUB', {'word': 'russian ruble',
             'symbol': '₽ (RUB)'}),
))

FOREIGN_CURRENCIES = OrderedDict((
    ('USD', {'word': 'american dollars',
             'symbol': 'American Dollar $ (USD)'}),
    ('EUR', {'word': 'euro',
             'symbol': 'Euro € (EUR)'}),
    ('GBP', {'word': 'british pounds',
             'symbol': 'British Pounds £ (GBP)'}),
    ('CAD', {'word': 'canadian dollars',
             'symbol': 'Canadian Dollar C$ (CAD)'}),
    ('RUB', {'word': 'russian ruble',
             'symbol': 'Russian Ruble ₽ (RUB)'}),
    ('AUD', {'word': 'australian dollars',
             'symbol': 'Australian Dollar A$ (AUD)'}),
    ('CNY', {'word': 'chinese yuan',
             'symbol': 'Chinese Yuan ¥ (CNY)'}),
    ('JPY', {'word': 'yapanese yen',
             'symbol': 'Japanase Yen ¥ (JPY)'}),
    ('THB', {'word': 'thai baht',
             'symbol': 'Thai Baht ฿ (THB)'}),
    ('SGD', {'word': 'singaporean dollar',
             'symbol': 'Singaporean Dollar S$ (SGD)'}),
    ('MYR', {'word': 'malaysian ringgit',
             'symbol': 'Malaysian Ringgit RM (MYR)'}),
    ('ZAR', {'word': 'south african rand',
             'symbol': 'South African Rand R (ZAR)'}),
))
