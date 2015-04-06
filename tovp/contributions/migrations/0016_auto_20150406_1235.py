# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0015_auto_20150405_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='is_external',
            field=models.BooleanField(db_index=True, verbose_name='Non Mayapur TOVP receipt', help_text='This MUST be checked if other than India TOVP receipt was given.', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pledge',
            name='currency',
            field=models.CharField(max_length=6, choices=[('INR', '₹ (INR)'), ('USD', '$ (USD)'), ('EUR', '€ (EUR)'), ('GBP', '£ (GBP)')], verbose_name='Currency', default='INR'),
            preserve_default=True,
        ),
    ]
