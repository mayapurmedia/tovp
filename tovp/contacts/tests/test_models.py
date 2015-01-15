from django.test import TestCase

from ..models import Person


class PersonModelTests(TestCase):
    def setUp(self):
        self.contact1 = Person.objects.create(
            title='Dr',
            first_name='Jay', middle_name='Sri', last_name='Narasimhadeva',
            initiated_name='Narasimha Das', email='nd@test.com',
            phone_number='+420333123456', address='Govinda Street 108',
            city='Sridham Mayapur', state='West Bengal', postcode='741313',
            country='IN', pan_card_number='ABCDE1234F'
        )

    def test_name(self):
        # test with only first and last name
        test_person = Person(first_name='Jay', last_name='Narasimhadeva')
        self.assertEqual(test_person.name, 'Jay Narasimhadeva')

        # test first, middle and last name
        test_person = Person(first_name='Jay', middle_name='Sri',
                             last_name='Narasimhadeva')
        self.assertEqual(test_person.name, 'Jay Sri Narasimhadeva')

    def test_full_name(self):
        test_person = Person(first_name='Jay', middle_name='Sri',
                             last_name='Narasimhadeva', title='Dr')
        self.assertEqual(test_person.full_name, 'Dr Jay Sri Narasimhadeva')
