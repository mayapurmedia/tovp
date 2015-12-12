import datetime

from django import forms
from django.test import TestCase
from django.http import HttpRequest
from jinja2 import Markup

from ..templatetags.core_tags import (
    active_link_class, format_with_commas, format_date, add_css, num2words,
    makeplain, update_url_query)


class AnantaHelpersTests(TestCase):
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

    def test_format_date(self):
        test_date = datetime.datetime(2001, 1, 31, 22, 10, 33)

        # test default filter
        self.assertEqual('31 January, 2001', format_date(test_date))
        # use custom filters
        self.assertEqual('2001', format_date(test_date, '%Y'))
        self.assertEqual('2001-01-31', format_date(test_date, '%Y-%m-%d'))
        self.assertEqual('22:10:33', format_date(test_date, '%H:%M:%S'))

    def test_add_css(self):
        class TestForm(forms.Form):
            char_field = forms.CharField(max_length=14)
            boolean_field = forms.BooleanField(required=False)

        form = TestForm()

        self.assertEqual(
            form['boolean_field'].as_widget(),
            '<input id="id_boolean_field" name="boolean_field" '
            'type="checkbox" />')

        self.assertEqual(
            add_css(form['boolean_field'], 'test-class'),
            '<input class="test-class" id="id_boolean_field" '
            'name="boolean_field" type="checkbox" />')

    def test_num2words(self):
        self.assertEqual(num2words(1), 'one')
        self.assertEqual(num2words(2), 'two')
        self.assertEqual(num2words(30), 'thirty')
        self.assertEqual(num2words(444), 'four hundred and forty-four')

    def test_makeplain(self):
        text = (
            'Text for testing <strong>makeplain</strong> filter. It should be '
            'able to strip tags and trim your <em>text</em>. When text is too '
            'long it will trim and add <span class="test">...</span>.'
        )
        expected_text = (
            'Text for testing makeplain filter. It should be able to stri...'
        )
        self.assertEqual(makeplain(text, 65, 60), expected_text)

    def test_update_url_query(self):
        self.assertEqual(update_url_query('/test', {'arg1': 108}),
                         '/test?arg1=108')
        self.assertEqual(update_url_query('/test?arg1=108', {'arg1': 'changed'}),
                         '/test?arg1=changed')
        self.assertEqual(update_url_query('/test?arg1=108', {'arg1': None}),
                         '/test')

        # test with multiple arguments
        self.assertEqual(update_url_query('/test?arg2=64', {'arg1': 108}),
                         '/test?arg1=108&arg2=64')
        self.assertEqual(update_url_query('/test?arg2=64&arg1=108',
                                          {'arg1': 'changed'}),
                         '/test?arg1=changed&arg2=64')
        self.assertEqual(update_url_query('/test?arg2=64&arg1=108',
                                          {'arg1': None}),
                         '/test?arg2=64')

        self.assertEqual(update_url_query('/test', {'arg1': 4, 'arg2': 6}),
                         '/test?arg1=4&arg2=6')
        self.assertEqual(update_url_query('/test?arg2=64&arg1=108',
                                          {'arg1': 'changed', 'arg2': 'also'}),
                         '/test?arg1=changed&arg2=also')
        self.assertEqual(update_url_query('/test?arg2=64&arg1=108',
                                          {'arg1': None, 'arg2': None}),
                         '/test')
