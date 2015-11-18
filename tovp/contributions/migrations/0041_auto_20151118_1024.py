# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0040_auto_20151117_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulkpayment',
            name='foreign_currency',
            field=models.CharField(default='INR', choices=[('INR', '₹ (INR)'), ('USD', '$ (USD)'), ('EUR', '€ (EUR)'), ('GBP', '£ (GBP)'), ('CAD', 'C$ (CAD)'), ('RUB', '\u20bd (RUB)')], max_length=6, help_text='Please fill if donation is coming fromforeign currency.', verbose_name='Foreign Currency'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contribution',
            name='foreign_currency',
            field=models.CharField(default='INR', choices=[('INR', '₹ (INR)'), ('USD', '$ (USD)'), ('EUR', '€ (EUR)'), ('GBP', '£ (GBP)'), ('CAD', 'C$ (CAD)'), ('RUB', '\u20bd (RUB)')], max_length=6, help_text='Please fill if donation is coming fromforeign currency.', verbose_name='Foreign Currency'),
            preserve_default=True,
        ),
    ]
