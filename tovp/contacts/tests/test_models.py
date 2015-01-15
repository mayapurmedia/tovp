from django.test import TestCase

from ..models import Person


class PersonModelTests(TestCase):
    def setUp(self):
        self.person = Person.objects.create(
            title='Dr',
            first_name='Jay', middle_name='Sri', last_name='Narasimhadeva',
            initiated_name='Narasimha Das', email='nd@test.com',
            phone_number='+420333123456', address='Govinda Street 108',
            city='Sridham Mayapur', state='West Bengal', postcode='741313',
            country='IN', pan_card_number='ABCDE1234F'
        )

    def test_name(self):
        # test first, middle and last name
        self.assertEqual(self.person.name, 'Jay Sri Narasimhadeva')

        # test with only first and last name
        self.person.middle_name = None
        self.assertEqual(self.person.name, 'Jay Narasimhadeva')

    def test_full_name(self):
        self.assertEqual(self.person.full_name, 'Dr Jay Sri Narasimhadeva')

    def test_full_address(self):
        self.assertEqual(
            self.person.full_address(), [
                'Govinda Street 108',
                'Sridham Mayapur',
                'West Bengal',
                '741313',
                'India'])
        self.assertEqual(
            self.person.full_address(include_full_name=True), [
                'Dr Jay Sri Narasimhadeva',
                'Govinda Street 108',
                'Sridham Mayapur',
                'West Bengal',
                '741313',
                'India'])
        # testing without country
        self.person.country = None
        self.assertEqual(
            self.person.full_address(), [
                'Govinda Street 108',
                'Sridham Mayapur',
                'West Bengal',
                '741313'])
