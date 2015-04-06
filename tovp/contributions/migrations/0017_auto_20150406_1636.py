# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0016_auto_20150406_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='currency',
            field=models.CharField(default='INR', verbose_name='Currency', choices=[('INR', '₹ (INR)'), ('USD', '$ (USD)'), ('EUR', '€ (EUR)'), ('GBP', '£ (GBP)')], max_length=6),
            preserve_default=True,
        ),
    ]
