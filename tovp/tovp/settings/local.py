# -*- coding: utf-8 -*-
'''
Local Configurations

- Runs in Debug mode
- Uses console backend for emails
- Use Django Debug Toolbar
'''
import os
from os.path import join

import dj_database_url

from .base import *  # noqa


# DEBUG
DEBUG = True
# END DEBUG

# Mail settings
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')
# End mail settings

# django-debug-toolbar
# MIDDLEWARE_CLASSES = Common.MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware',)
# INSTALLED_APPS += ('debug_toolbar',)

# INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)

# DEBUG_TOOLBAR_CONFIG = {
#     'DISABLE_PANELS': [
#         'debug_toolbar.panels.redirects.RedirectsPanel',
#     ],
#     'SHOW_TEMPLATE_CONTEXT': True,
# }
# # end django-debug-toolbar

# DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': join(BASE_DIR, 'db.sqlite3'),
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': '',
#         'PORT': '',
#     }
# }
# END DATABASE CONFIGURATION
DATABASES = {'default': dj_database_url.config(default='sqlite:///%s' % join(BASE_DIR, '../db.sqlite3'))}

# ABSOLUTE_DOMAIN = '//donate.tovp.org'

# Your local stuff: Below this line define 3rd party libary settings
