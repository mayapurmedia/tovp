# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0050_auto_20160411_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulkpayment',
            name='payment_method',
            field=models.CharField(choices=[('cashl', 'Cash (Indian)'), ('cashf', 'Cash (Foreign)'), ('cashd', 'Cash Deposit'), ('ccdcsl', 'Credit/Debit Card Swipe Local'), ('ccdcsf', 'Credit/Debit Card Swipe Foreign'), ('neftl', 'NEFT (Indian)'), ('neftf', 'NEFT/Bank Transfer (Foreign)'), ('chequel', 'Cheque (Indian)'), ('chequef', 'Cheque (Foreign)'), ('chequed', 'Cheque Deposit'), ('paypal', 'Paypal'), ('axis', 'Gateway Axis (Internet)'), ('treasury', 'ISKCON Treasury'), ('bulk', 'Part of the Bulk Payment')], verbose_name='Payment Method', max_length=16),
        ),
        migrations.AlterField(
            model_name='contribution',
            name='payment_method',
            field=models.CharField(choices=[('cashl', 'Cash (Indian)'), ('cashf', 'Cash (Foreign)'), ('cashd', 'Cash Deposit'), ('ccdcsl', 'Credit/Debit Card Swipe Local'), ('ccdcsf', 'Credit/Debit Card Swipe Foreign'), ('neftl', 'NEFT (Indian)'), ('neftf', 'NEFT/Bank Transfer (Foreign)'), ('chequel', 'Cheque (Indian)'), ('chequef', 'Cheque (Foreign)'), ('chequed', 'Cheque Deposit'), ('paypal', 'Paypal'), ('axis', 'Gateway Axis (Internet)'), ('treasury', 'ISKCON Treasury'), ('bulk', 'Part of the Bulk Payment')], verbose_name='Payment Method', max_length=16),
        ),
    ]
