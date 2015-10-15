# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0035_auto_20150928_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulkpayment',
            name='currency',
            field=models.CharField(max_length=6, default='INR', choices=[('INR', '₹ (INR)'), ('USD', '$ (USD)'), ('EUR', '€ (EUR)'), ('GBP', '£ (GBP)'), ('CAD', 'C$ (CAD)')], verbose_name='Currency'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contribution',
            name='currency',
            field=models.CharField(max_length=6, default='INR', choices=[('INR', '₹ (INR)'), ('USD', '$ (USD)'), ('EUR', '€ (EUR)'), ('GBP', '£ (GBP)'), ('CAD', 'C$ (CAD)')], verbose_name='Currency'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pledge',
            name='currency',
            field=models.CharField(max_length=6, default='INR', choices=[('INR', '₹ (INR)'), ('USD', '$ (USD)'), ('EUR', '€ (EUR)'), ('GBP', '£ (GBP)'), ('CAD', 'C$ (CAD)')], verbose_name='Currency'),
            preserve_default=True,
        ),
    ]
