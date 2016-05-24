import os
import csv
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
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
    )

    help = 'Replaces emails of contacts with data from csv file.'

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
                # print('=*', row['original'])
                contacts = Person.objects.all().filter(email=row['original'])
                for contact in contacts:
                    if row['original'] == row['corrected']:
                        row['corrected'] = ''

                    contact.email = row['corrected']
                    print('%s \t====> %s' % (row['original'], contact.email))
                    contact.save()
                    count += 1
        print('Changed %d contacts.' % count)
