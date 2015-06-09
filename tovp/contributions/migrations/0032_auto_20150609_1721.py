# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0031_auto_20150605_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulkpayment',
            name='note',
            field=models.TextField(max_length=255, verbose_name='Note', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contribution',
            name='note',
            field=models.TextField(max_length=255, verbose_name='Note', blank=True),
            preserve_default=True,
        ),
    ]
