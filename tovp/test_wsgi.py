from django.test import TestCase
from django.core.handlers.wsgi import WSGIHandler

from .wsgi import application


class WSGITestCase(TestCase):
    def test_wsgi(self):
        " Test my custom command."
        self.assertIsInstance(application, WSGIHandler)
