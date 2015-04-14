# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0022_auto_20150413_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulkpayment',
            name='overwrite_pan_card',
            field=models.CharField(null=True, verbose_name='Overwrite PAN card number', max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contribution',
            name='overwrite_pan_card',
            field=models.CharField(null=True, verbose_name='Overwrite PAN card number', max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
