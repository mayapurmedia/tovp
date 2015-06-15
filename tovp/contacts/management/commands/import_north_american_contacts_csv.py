import os
import csv
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

from ...models import Person


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option(
            "-f",
            "--file",
            dest="filename",
            help="Specify import file",
            metavar="FILE"),
        make_option(
            "-l",
            "--location",
            dest="location",
            help="Specify location of collection"),
    )

    help = 'Imports contacts from North American csv files.'

    def handle(self, *args, **options):
        # make sure file option is present
        if options['filename'] is None:
            raise CommandError("Option `--file=...` must be specified.")

        # make sure file path resolves
        if not os.path.isfile(options['filename']):
            raise CommandError("File does not exist at the specified path.")

        self.stdout.write("Opening input file...")

        user = get_user_model().objects.get(pk=1)
        count = 0
        with open(options['filename']) as csvfile:
            csv_reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
            for row in csv_reader:
                field_names = {
                    'Temple': 'temple',
                    'Spiritual Name': 'initiated_name',
                    'First Name': 'first_name',
                    'Middle Name': 'middle_name',
                    'Last Name': 'last_name',
                    'Phone': 'phone_number',
                    'Email': 'email',
                    'Street Address': 'address',
                    'City': 'city',
                    'State': 'state',
                    'Zip Code': 'postcode',
                }

                kwargs = {}
                for field in field_names:
                    if row[field]:
                        kwargs[field_names[field]] = row[field]
                        # setattr(person, field_names[field], row[field].strip())
                try:
                    person = Person.objects.get(country='US', pan_card_number='', **kwargs)
                except ObjectDoesNotExist:
                    person = Person(country='US', yatra='north-america',
                                    pan_card_number='', **kwargs)
                    if options['location']:
                        person.location = options['location']

                    person.created_by = user

                    if (person.first_name and person.last_name) or person.initiated_name:
                        person.save()
                    else:
                        print('ERROR - skipping, record missing name')
                    count += 1
                except:
                    pass
                print(person.pk)
        print('Imported %d new contacts.' % count)
