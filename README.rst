TOVP
==============================

Temple Of The Vedic Planetarium Fundraising Website

[![Build Status](https://travis-ci.org/mayapurmedia/tovp.svg?branch=master)](https://travis-ci.org/mayapurmedia/tovp)
[![Coverage Status](https://coveralls.io/repos/mayapurmedia/tovp/badge.png?branch=master)](https://coveralls.io/r/mayapurmedia/tovp?branch=master)
[![Django Version]](http://img.shields.io/badge/django-v1.7.1-blue.svg)
[![License]](http://img.shields.io/badge/license-MIT-green.svg)

Settings
------------

TOVP relies extensively on environment settings which **will not work with Apache/mod_wsgi setups**. It has been deployed successfully with both Gunicorn/Nginx and even uWSGI/Nginx.

For configuration purposes, the following table maps the 'TOVP' environment variables to their Django setting:

======================================= =========================== ============================================== ===========================================
Environment Variable                    Django Setting              Development Default                            Production Default
======================================= =========================== ============================================== ===========================================
DJANGO_CACHES                           CACHES                      locmem                                         memcached
DJANGO_DATABASES                        DATABASES                   See code                                       See code
DJANGO_DEBUG                            DEBUG                       True                                           False
DJANGO_EMAIL_BACKEND                    EMAIL_BACKEND               django.core.mail.backends.console.EmailBackend django.core.mail.backends.smtp.EmailBackend
DJANGO_SECRET_KEY                       SECRET_KEY                  CHANGEME!!!                                    raises error
DJANGO_SECURE_BROWSER_XSS_FILTER        SECURE_BROWSER_XSS_FILTER   n/a                                            True
DJANGO_SECURE_SSL_REDIRECT              SECURE_SSL_REDIRECT         n/a                                            True
DJANGO_SECURE_CONTENT_TYPE_NOSNIFF      SECURE_CONTENT_TYPE_NOSNIFF n/a                                            True
DJANGO_SECURE_FRAME_DENY                SECURE_FRAME_DENY           n/a                                            True
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS   HSTS_INCLUDE_SUBDOMAINS     n/a                                            True
DJANGO_SESSION_COOKIE_HTTPONLY          SESSION_COOKIE_HTTPONLY     n/a                                            True
DJANGO_SESSION_COOKIE_SECURE            SESSION_COOKIE_SECURE       n/a                                            False
======================================= =========================== ============================================== ===========================================


Getting up and running
----------------------

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* pip
* virtualenv
@@@@@@@@@@@@@ * PostgreSQL

First make sure to create and activate a virtualenv_, then open a terminal at the project root and install the requirements for local development::

    $ pip install -r requirements/local.txt

.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/

You can now run the usual Django ``runserver`` command (replace ``yourapp`` with the name of the directory containing the Django project)::

    $ python yourapp/manage.py runserver

