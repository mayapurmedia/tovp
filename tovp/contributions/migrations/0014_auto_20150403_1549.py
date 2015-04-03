# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0013_pledge_number_of_instalments'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribution',
            name='source',
            field=models.CharField(max_length=30, default='', verbose_name='Source', blank=True, choices=[('nityananda', 'Nityananda Tour'), ('jps-office', 'JPS Office'), ('namahatta', 'JPS Namahatta'), ('jps-others', 'JPS Others'), ('mso', 'M.S.O.'), ('lm-reception', 'Life Membership Reception'), ('vrindavan-booth', 'Vrindavan'), ('other', 'Other')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pledge',
            name='source',
            field=models.CharField(max_length=30, default='', verbose_name='Source', blank=True, choices=[('nityananda', 'Nityananda Tour'), ('jps-office', 'JPS Office'), ('namahatta', 'JPS Namahatta'), ('jps-others', 'JPS Others'), ('mso', 'M.S.O.'), ('lm-reception', 'Life Membership Reception'), ('vrindavan-booth', 'Vrindavan'), ('other', 'Other')]),
            preserve_default=True,
        ),
    ]
