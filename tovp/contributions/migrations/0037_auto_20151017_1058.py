# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0036_auto_20151015_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulkpayment',
            name='currency',
            field=models.CharField(verbose_name='Currency', choices=[('INR', '₹ (INR)'), ('USD', '$ (USD)'), ('EUR', '€ (EUR)'), ('GBP', '£ (GBP)'), ('CAD', 'C$ (CAD)'), ('RUB', '\u20bd (RUB)')], default='INR', max_length=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contribution',
            name='currency',
            field=models.CharField(verbose_name='Currency', choices=[('INR', '₹ (INR)'), ('USD', '$ (USD)'), ('EUR', '€ (EUR)'), ('GBP', '£ (GBP)'), ('CAD', 'C$ (CAD)'), ('RUB', '\u20bd (RUB)')], default='INR', max_length=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pledge',
            name='currency',
            field=models.CharField(verbose_name='Currency', choices=[('INR', '₹ (INR)'), ('USD', '$ (USD)'), ('EUR', '€ (EUR)'), ('GBP', '£ (GBP)'), ('CAD', 'C$ (CAD)'), ('RUB', '\u20bd (RUB)')], default='INR', max_length=6),
            preserve_default=True,
        ),
    ]
