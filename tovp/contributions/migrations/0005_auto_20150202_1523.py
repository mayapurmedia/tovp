# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0004_auto_20150201_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribution',
            name='overwrite_address',
            field=models.CharField(max_length=255, verbose_name='Address who pays on behalf of main contact', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contribution',
            name='overwrite_name',
            field=models.CharField(max_length=255, verbose_name='Name who pays on behalf of main contact', blank=True),
            preserve_default=True,
        ),
    ]
