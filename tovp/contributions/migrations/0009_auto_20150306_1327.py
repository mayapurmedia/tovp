# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0008_auto_20150219_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribution',
            name='is_external',
            field=models.BooleanField(db_index=True, help_text='This MUST be checked if other than India TOVP receipt was given.', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pledge',
            name='interval',
            field=models.CharField(verbose_name='Payments Interval', max_length=30, help_text='Enter planned interval of payments (e.g. 1 month)', choices=[('1', '1 month'), ('2', '2 months'), ('3', '3 months'), ('4', '4 months'), ('6', '6 months'), ('12', '12 months')], default='1'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pledge',
            name='payments_start_date',
            field=models.DateField(blank=True, verbose_name='Payments Start', null=True, help_text='Date of first expected payment for this pledge.', default=datetime.datetime.now),
            preserve_default=True,
        ),
    ]
