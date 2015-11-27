# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0042_auto_20151120_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulkpayment',
            name='foreign_currency',
            field=models.CharField(max_length=6, verbose_name='Foreign Currency', default='INR', help_text='Please fill if donation is coming fromforeign currency.', choices=[('USD', 'American Dollar $ (USD)'), ('EUR', 'Euro € (EUR)'), ('GBP', 'British Pounds £ (GBP)'), ('CAD', 'Canadian Dollar C$ (CAD)'), ('RUB', 'Russian Ruble \u20bd (RUB)'), ('AUD', 'Australian Dollar A$ (AUD)'), ('CNY', 'Chinese Yuan ¥ (CNY)'), ('JPY', 'Japanase Yen ¥ (JPY)'), ('THB', 'Thai Baht ฿ (THB)'), ('SGD', 'Singaporean Dollar S$ (SGD)'), ('MYR', 'Malaysian Ringgit RM (MYR)'), ('ZAR', 'South African Rand R (ZAR)')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contribution',
            name='foreign_currency',
            field=models.CharField(max_length=6, verbose_name='Foreign Currency', default='INR', help_text='Please fill if donation is coming fromforeign currency.', choices=[('USD', 'American Dollar $ (USD)'), ('EUR', 'Euro € (EUR)'), ('GBP', 'British Pounds £ (GBP)'), ('CAD', 'Canadian Dollar C$ (CAD)'), ('RUB', 'Russian Ruble \u20bd (RUB)'), ('AUD', 'Australian Dollar A$ (AUD)'), ('CNY', 'Chinese Yuan ¥ (CNY)'), ('JPY', 'Japanase Yen ¥ (JPY)'), ('THB', 'Thai Baht ฿ (THB)'), ('SGD', 'Singaporean Dollar S$ (SGD)'), ('MYR', 'Malaysian Ringgit RM (MYR)'), ('ZAR', 'South African Rand R (ZAR)')]),
            preserve_default=True,
        ),
    ]
