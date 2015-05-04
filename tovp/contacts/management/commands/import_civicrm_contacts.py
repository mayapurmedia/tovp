import os
import re
import csv
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

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

        countries_list = {
            'Afghanistan': 'AF',
            'Albania': 'AL',
            'Algeria': 'DZ',
            'American Samoa': 'AS',
            'Andorra': 'AD',
            'Angola': 'AO',
            'Anguilla': 'AI',
            'Antarctica': 'AQ',
            'Antigua and Barbuda': 'AG',
            'Argentina': 'AR',
            'Armenia': 'AM',
            'Aruba': 'AW',
            'Australia': 'AU',
            'Austria': 'AT',
            'Azerbaijan': 'AZ',
            'Bahrain': 'BH',
            'Bangladesh': 'BD',
            'Barbados': 'BB',
            'Belarus': 'BY',
            'Belgium': 'BE',
            'Belize': 'BZ',
            'Benin': 'BJ',
            'Bermuda': 'BM',
            'Bhutan': 'BT',
            'Bolivia': 'BO',
            'Bosnia and Herzegovina': 'BA',
            'Botswana': 'BW',
            'Bouvet Island': 'BV',
            'Brazil': 'BR',
            'British Indian Ocean Territory': 'IO',
            'Virgin Islands, British': 'VG',
            'Brunei Darussalam': 'BN',
            'Bulgaria': 'BG',
            'Burkina Faso': 'BF',
            'Myanmar': 'MM',
            'Burundi': 'BI',
            'Cambodia': 'KH',
            'Cameroon': 'CM',
            'Canada': 'CA',
            'Cape Verde': 'CV',
            'Cayman Islands': 'KY',
            'Central African Republic': 'CF',
            'Chad': 'TD',
            'Chile': 'CL',
            'China': 'CN',
            'Christmas Island': 'CX',
            'Cocos (Keeling) Islands': 'CC',
            'Colombia': 'CO',
            'Comoros': 'KM',
            'Congo, The Democratic Republic of the': 'CD',
            'Congo, Republic of the': 'CG',
            'Cook Islands': 'CK',
            'Costa Rica': 'CR',
            'Côte d\'Ivoire': 'CI',
            'Croatia': 'HR',
            'Cuba': 'CU',
            'Cyprus': 'CY',
            'Czech Republic': 'CZ',
            'Denmark': 'DK',
            'Djibouti': 'DJ',
            'Dominica': 'DM',
            'Dominican Republic': 'DO',
            'Timor-Leste': 'TL',
            'Ecuador': 'EC',
            'Egypt': 'EG',
            'El Salvador': 'SV',
            'Equatorial Guinea': 'GQ',
            'Eritrea': 'ER',
            'Estonia': 'EE',
            'Ethiopia': 'ET',
            'Falkland Islands (Malvinas)': 'FK',
            'Faroe Islands': 'FO',
            'Fiji': 'FJ',
            'Finland': 'FI',
            'France': 'FR',
            'French Guiana': 'GF',
            'French Polynesia': 'PF',
            'French Southern Territories': 'TF',
            'Gabon': 'GA',
            'Georgia': 'GE',
            'Germany': 'DE',
            'Ghana': 'GH',
            'Gibraltar': 'GI',
            'Greece': 'GR',
            'Greenland': 'GL',
            'Grenada': 'GD',
            'Guadeloupe': 'GP',
            'Guam': 'GU',
            'Guatemala': 'GT',
            'Guinea': 'GN',
            'Guinea-Bissau': 'GW',
            'Guyana': 'GY',
            'Haiti': 'HT',
            'Heard Island and McDonald Islands': 'HM',
            'Holy See (Vatican City State)': 'VA',
            'Honduras': 'HN',
            'Hong Kong': 'HK',
            'Hungary': 'HU',
            'Iceland': 'IS',
            'India': 'IN',
            'Indonesia': 'ID',
            'Iran, Islamic Republic of': 'IR',
            'Iraq': 'IQ',
            'Ireland': 'IE',
            'Israel': 'IL',
            'Italy': 'IT',
            'Jamaica': 'JM',
            'Japan': 'JP',
            'Jordan': 'JO',
            'Kazakhstan': 'KZ',
            'Kenya': 'KE',
            'Kiribati': 'KI',
            'Korea, Democratic People\'s Republic of': 'KP',
            'Korea, Republic of': 'KR',
            'Kuwait': 'KW',
            'Kyrgyzstan': 'KG',
            'Lao People\'s Democratic Republic': 'LA',
            'Latvia': 'LV',
            'Lebanon': 'LB',
            'Lesotho': 'LS',
            'Liberia': 'LR',
            'Libya': 'LY',
            'Liechtenstein': 'LI',
            'Lithuania': 'LT',
            'Luxembourg': 'LU',
            'Macao': 'MO',
            'Macedonia, Republic of': 'MK',
            'Madagascar': 'MG',
            'Malawi': 'MW',
            'Malaysia': 'MY',
            'Maldives': 'MV',
            'Mali': 'ML',
            'Malta': 'MT',
            'Marshall Islands': 'MH',
            'Martinique': 'MQ',
            'Mauritania': 'MR',
            'Mauritius': 'MU',
            'Mayotte': 'YT',
            'Mexico': 'MX',
            'Micronesia, Federated States of': 'FM',
            'Moldova': 'MD',
            'Monaco': 'MC',
            'Mongolia': 'MN',
            'Montserrat': 'MS',
            'Morocco': 'MA',
            'Mozambique': 'MZ',
            'Namibia': 'NA',
            'Nauru': 'NR',
            'Nepal': 'NP',
            'Netherlands': 'NL',
            'New Caledonia': 'NC',
            'New Zealand': 'NZ',
            'Nicaragua': 'NI',
            'Niger': 'NE',
            'Nigeria': 'NG',
            'Niue': 'NU',
            'Norfolk Island': 'NF',
            'Northern Mariana Islands': 'MP',
            'Norway': 'NO',
            'Oman': 'OM',
            'Pakistan': 'PK',
            'Palau': 'PW',
            'Palestinian Territory, Occupied': 'PS',
            'Panama': 'PA',
            'Papua New Guinea': 'PG',
            'Paraguay': 'PY',
            'Peru': 'PE',
            'Philippines': 'PH',
            'Pitcairn': 'PN',
            'Poland': 'PL',
            'Portugal': 'PT',
            'Puerto Rico': 'PR',
            'Qatar': 'QA',
            'Romania': 'RO',
            'Russian Federation': 'RU',
            'Rwanda': 'RW',
            'Reunion': 'RE',
            'Saint Helena': 'SH',
            'Saint Kitts and Nevis': 'KN',
            'Saint Lucia': 'LC',
            'Saint Pierre and Miquelon': 'PM',
            'Saint Vincent and the Grenadines': 'VC',
            'Samoa': 'WS',
            'San Marino': 'SM',
            'Saudi Arabia': 'SA',
            'Senegal': 'SN',
            'Seychelles': 'SC',
            'Sierra Leone': 'SL',
            'Singapore': 'SG',
            'Slovakia': 'SK',
            'Slovenia': 'SI',
            'Solomon Islands': 'SB',
            'Somalia': 'SO',
            'South Africa': 'ZA',
            'South Georgia and the South Sandwich Islands': 'GS',
            'Spain': 'ES',
            'Sri Lanka': 'LK',
            'Sudan': 'SD',
            'Suriname': 'SR',
            'Svalbard and Jan Mayen': 'SJ',
            'Swaziland': 'SZ',
            'Sweden': 'SE',
            'Switzerland': 'CH',
            'Syrian Arab Republic': 'SY',
            'Sao Tome and Principe': 'ST',
            'Taiwan': 'TW',
            'Tajikistan': 'TJ',
            'Tanzania, United Republic of': 'TZ',
            'Thailand': 'TH',
            'Bahamas': 'BS',
            'Gambia': 'GM',
            'Togo': 'TG',
            'Tokelau': 'TK',
            'Tonga': 'TO',
            'Trinidad and Tobago': 'TT',
            'Tunisia': 'TN',
            'Turkey': 'TR',
            'Turkmenistan': 'TM',
            'Turks and Caicos Islands': 'TC',
            'Tuvalu': 'TV',
            'Uganda': 'UG',
            'Ukraine': 'UA',
            'United Arab Emirates': 'AE',
            'United Kingdom': 'GB',
            'United States Minor Outlying Islands': 'UM',
            'United States': 'US',
            'Uruguay': 'UY',
            'Uzbekistan': 'UZ',
            'Vanuatu': 'VU',
            'Venezuela': 'VE',
            'Viet Nam': 'VN',
            'Virgin Islands, U.S.': 'VI',
            'Wallis and Futuna': 'WF',
            'Western Sahara': 'EH',
            'Yemen': 'YE',
            'Serbia and Montenegro': 'CS',
            'Zambia': 'ZM',
            'Zimbabwe': 'ZW',
            'Åland Islands': 'AX',
            'Serbia': 'RS',
            'Montenegro': 'ME',
            'Jersey': 'JE',
            'Guernsey': 'GG',
            'Isle of Man': 'IM',
            'South Sudan': 'SS',
            'Curaçao': 'CW',
            'Sint Maarten (Dutch Part)': 'SX',
            'Bonaire, Saint Eustatius and Saba': 'BQ',
            'Kosovo': 'XK',
        }

        # make sure file option is present
        if options['filename'] is None:
            raise CommandError("Option `--file=...` must be specified.")

        # make sure file path resolves
        if not os.path.isfile(options['filename']):
            raise CommandError("File does not exist at the specified path.")

        self.stdout.write("Opening input file...")

        user = get_user_model().objects.get(pk=1)
        count = 0

        pan_card_validation = re.compile('[A-Za-z]{5}\d{4}[A-Za-z]{1}')
        email_validation = re.compile('(mayapur.none@com|none@valentina|no@e?mail\.com|.*@n|.*@(a?nonec?(.c?om)?(.com)?(.in)?|nomail(.com)?)|s?nomail@.*)$')

        with open(options['filename']) as csvfile:
            csv_reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
            for row in csv_reader:
                kwargs = {}

                pan_card_number = row["PAN Number"].replace(' ', '')
                if (pan_card_number):
                    if not pan_card_validation.match(pan_card_number):
                        pan_card_number = ''
                kwargs['pan_card_number'] = pan_card_number

                email = row['Home-Email']
                if (email):
                    if email_validation.match(email):
                        email = ''
                    else:
                        kwargs['email'] = email

                country = row["Home-Country"]
                if country:
                    kwargs['country'] = countries_list[country]

                old_database_id = int(row["Internal Contact ID"])
                kwargs['old_database_id'] = old_database_id

                kwargs['first_name'] = row["First Name"].strip()
                kwargs['middle_name'] = row["Middle Name"].strip()
                kwargs['last_name'] = row["Last Name"].strip()
                kwargs['initiated_name'] = row["Nickname"].strip()

                phone_number = row["Home-Phone-Phone"]
                if phone_number not in ['n/a', 'n']:
                    kwargs['phone_number'] = phone_number.strip()

                kwargs['city'] = row["Home-City"].strip()
                kwargs['state'] = row["Home-State"].strip()

                address = ', '.join(filter(bool, [
                    row["Home-Street Address"].strip(),
                    row["Home-Supplemental Address 1"].strip(),
                    row["Home-Supplemental Address 2"].strip()]))
                if address:
                    kwargs['address'] = address

                postcode = '-'.join(filter(bool, [
                    row["Home-Postal Code"].strip(),
                    row["Home-Postal Code Suffix"].strip()]))
                if address:
                    kwargs['postcode'] = postcode

                try:
                    person = Person.objects.get(**kwargs)
                except:
                    person = Person(**kwargs)

                    if not (person.first_name or person.last_name or
                            person.middle_name or person.initiated_name):
                        person.initiated_name = 'NoNameFromOldDatabase'

                    person.created_by = user
                    person.save()
                count += 1
                if not person.pk:
                    print('ERROR - not created %d' % person.old_database_id)
        print('Imported %d new contacts.' % count)
