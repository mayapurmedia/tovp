import os
import csv
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError

from ...models import Person


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option(
            "-f",
            "--file",
            dest="filename",
            help="Specify import file",
            metavar="FILE"),
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

        count = 0
        with open(options['filename']) as csvfile:
            csv_reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
            for row in csv_reader:
                field_names = {
                    'Spiritual Name': 'initiated_name',
                    'First Name': 'first_name',
                    'Middle Name': 'middle_name',
                    'Last Name': 'last_name',
                    'City': 'city',
                    'Street Address': 'address',
                    'Zip Code': 'postcode',
                    'State': 'state',
                    'email': 'email',
                    'Phone ': 'phone_number',
                }

                kwargs = {}
                for field in field_names:
                    if row[field]:
                        kwargs[field_names[field]] = row[field]
                        # setattr(person, field_names[field], row[field].strip())
                try:
                    person = Person.objects.get(country='US', pan_card_number='', **kwargs)
                except:
                    person = Person(country='US', pan_card_number='', **kwargs)
                    person.save()
                    count += 1
                print(person.pk)
        print('Imported %d new contacts.' % count)
