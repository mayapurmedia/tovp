# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0014_auto_20150403_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='source',
            field=models.CharField(max_length=30, blank=True, default='', verbose_name='Source', choices=[('nityananda', 'Nityananda Tour'), ('jps-office', 'JPS Office'), ('namahatta', 'JPS Namahatta'), ('jps-others', 'JPS Others'), ('nvs', 'Nava Yogendra Swami'), ('mso', 'M.S.O.'), ('lm-reception', 'Life Membership Reception'), ('vrindavan-booth', 'Vrindavan Booth'), ('other', 'Other')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pledge',
            name='source',
            field=models.CharField(max_length=30, blank=True, default='', verbose_name='Source', choices=[('nityananda', 'Nityananda Tour'), ('jps-office', 'JPS Office'), ('namahatta', 'JPS Namahatta'), ('jps-others', 'JPS Others'), ('nvs', 'Nava Yogendra Swami'), ('mso', 'M.S.O.'), ('lm-reception', 'Life Membership Reception'), ('vrindavan-booth', 'Vrindavan Booth'), ('other', 'Other')]),
            preserve_default=True,
        ),
    ]
