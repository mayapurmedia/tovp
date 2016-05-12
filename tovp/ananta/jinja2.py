from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'settings': settings,
    })
    return env
