import datetime

from django import forms
from django.test import TestCase
from django.http import HttpRequest
from jinja2 import Markup

from ..helpers import now, active_link_class, format_with_commas, datetimeformat


class AnantaHelpersTests(TestCase):
    def test_now(self):
        # testing login
        self.assertEqual(now(), datetime.date.today().strftime("%d %B %Y"))
        self.assertEqual(now("%Y"), datetime.date.today().strftime("%Y"))

    def test_active_link_class(self):
        request = HttpRequest()
        request.path = '/'

        self.assertEqual(Markup(' active'),
                         active_link_class(request, '/'))
        # should return empty string for not matching pattern
        self.assertEqual('', active_link_class(request, '^/contacts/'))

        request.path = '/contacts/'
        self.assertEqual('', active_link_class(request, '^/$'))
        self.assertEqual(Markup(' active'),
                         active_link_class(request, '^/contacts/'))

    def test_format_with_commas(self):
        self.assertEqual('0.1234', format_with_commas(.1234, '%.4f'))
        self.assertEqual('100', format_with_commas(100, '%i'))
        self.assertEqual('234.5678', format_with_commas(234.5678, '%.4f'))
        self.assertEqual('$234.5678', format_with_commas(234.5678, '$%.4f'))
        self.assertEqual('1,000', format_with_commas(1000, '%i'))
        self.assertEqual('1,234.5678', format_with_commas(1234.5678, '%.4f'))
        self.assertEqual('$1,234.5678', format_with_commas(1234.5678, '$%.4f'))
        self.assertEqual('1,000,000', format_with_commas(1000000, '%i'))
        self.assertEqual('1,234,567.5678', format_with_commas(1234567.5678,
                                                              '%.4f'))
        self.assertEqual('$1,234,567.5678', format_with_commas(1234567.5678,
                                                               '$%.4f'))
        self.assertEqual('-100', format_with_commas(-100, '%i'))
        self.assertEqual('-234.5678', format_with_commas(-234.5678, '%.4f'))
        self.assertEqual('$-234.5678', format_with_commas(-234.5678, '$%.4f'))
        self.assertEqual('-1,000', format_with_commas(-1000, '%i'))
        self.assertEqual('-1,234.5678', format_with_commas(-1234.5678, '%.4f'))
        self.assertEqual('$-1,234.5678', format_with_commas(-1234.5678,
                                                            '$%.4f'))
        self.assertEqual('-1,000,000', format_with_commas(-1000000, '%i'))
        self.assertEqual('-1,234,567.5678', format_with_commas(-1234567.5678,
                                                               '%.4f'))
        self.assertEqual('$-1,234,567.5678', format_with_commas(-1234567.5678,
                                                                '$%.4f'))

    def test_datetimeformat(self):
        test_date = datetime.datetime(2001, 1, 31, 22, 10, 33)

        # test default filter
        self.assertEqual('Jan 31 2001', datetimeformat(test_date))
        # use custom filters
        self.assertEqual('2001', datetimeformat(test_date, '%Y'))
        self.assertEqual('2001-01-31', datetimeformat(test_date, '%Y-%m-%d'))
        self.assertEqual('22:10:33', datetimeformat(test_date, '%H:%M:%S'))

    def test_add_css(self):
        class TestForm(forms.Form):
            char_field = forms.CharField(max_length=14)
            boolean_field = forms.BooleanField(required=False)

        form = TestForm()
        from ..helpers import add_css

        self.assertEqual(
            form['boolean_field'].as_widget(),
            '<input id="id_boolean_field" name="boolean_field" '
            'type="checkbox" />')

        self.assertEqual(
            add_css(form['boolean_field'], 'test-class'),
            '<input class="test-class" id="id_boolean_field" '
            'name="boolean_field" type="checkbox" />')
