# -*- coding: utf-8 -*-
'''
Production Configurations

- Use djangosecure
- Use Amazon's S3 for storing static files and uploaded media
- Use sendgrid to send emails
- Use MEMCACHIER on Heroku
'''
from .base import *  # noqa


# This ensures that Django will be able to detect a secure connection
# properly on Heroku.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# django-secure
INSTALLED_APPS += ("djangosecure", )

# set this to 60 seconds and then to 518400 when you can prove it works
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = bool(os.environ.get('SECURE_HSTS_INCLUDE_SUBDOMAINS', True))
SECURE_FRAME_DENY = bool(os.environ.get('SECURE_HSTS_INCLUDE_SUBDOMAINS', True))
SECURE_CONTENT_TYPE_NOSNIFF = bool(os.environ.get('SECURE_CONTENT_TYPE_NOSNIFF', True))
SECURE_BROWSER_XSS_FILTER = bool(os.environ.get('SECURE_BROWSER_XSS_FILTER', True))
SESSION_COOKIE_SECURE = bool(os.environ.get('SESSION_COOKIE_SECURE', True))
SESSION_COOKIE_HTTPONLY = bool(os.environ.get('SESSION_COOKIE_HTTPONLY', True))
SECURE_SSL_REDIRECT = bool(os.environ.get('SECURE_SSL_REDIRECT', True))
# end django-secure

# SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split()
ALLOWED_HOSTS = [
    "donate.tovp.org",
    "donate-playground.tovp.org"
]
# END SITE CONFIGURATION

# INSTALLED_APPS += ("gunicorn", )

# # STORAGE CONFIGURATION
# # See: http://django-storages.readthedocs.org/en/latest/index.html
# INSTALLED_APPS += (
#     'storages',
# )

# # See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
# STATICFILES_STORAGE = DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
# STATIC_URL = 'https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
# END STORAGE CONFIGURATION

# # EMAIL
# DEFAULT_FROM_EMAIL = values.Value('TOVP <noreply@donate.tovp.org>')
# EMAIL_HOST = values.Value('smtp.sendgrid.com')
# EMAIL_HOST_PASSWORD = values.SecretValue(environ_prefix="", environ_name="SENDGRID_PASSWORD")
# EMAIL_HOST_USER = values.SecretValue(environ_prefix="", environ_name="SENDGRID_USERNAME")
# EMAIL_PORT = values.IntegerValue(587, environ_prefix="", environ_name="EMAIL_PORT")
# EMAIL_SUBJECT_PREFIX = values.Value('[TOVP] ', environ_name="EMAIL_SUBJECT_PREFIX")
# EMAIL_USE_TLS = True
# SERVER_EMAIL = EMAIL_HOST_USER
# # END EMAIL

# # TEMPLATE CONFIGURATION
# # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
# TEMPLATE_LOADERS = (
#     ('django.template.loaders.cached.Loader', (
#         'django.template.loaders.filesystem.Loader',
#         'django.template.loaders.app_directories.Loader',
#     )),
# )
# # END TEMPLATE CONFIGURATION

# Your production stuff: Below this line define 3rd party libary settings
