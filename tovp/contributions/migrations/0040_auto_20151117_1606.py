# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0039_auto_20151101_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulkpayment',
            name='foreign_amount',
            field=models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Foreign Amount', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bulkpayment',
            name='foreign_currency',
            field=models.CharField(choices=[('INR', '₹ (INR)'), ('USD', '$ (USD)'), ('EUR', '€ (EUR)'), ('GBP', '£ (GBP)'), ('CAD', 'C$ (CAD)'), ('RUB', '\u20bd (RUB)')], max_length=6, verbose_name='Foreign Currency', default='INR'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contribution',
            name='foreign_amount',
            field=models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Foreign Amount', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contribution',
            name='foreign_currency',
            field=models.CharField(choices=[('INR', '₹ (INR)'), ('USD', '$ (USD)'), ('EUR', '€ (EUR)'), ('GBP', '£ (GBP)'), ('CAD', 'C$ (CAD)'), ('RUB', '\u20bd (RUB)')], max_length=6, verbose_name='Foreign Currency', default='INR'),
            preserve_default=True,
        ),
    ]
