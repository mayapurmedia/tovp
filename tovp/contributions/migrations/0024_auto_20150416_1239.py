# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0023_auto_20150414_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulkpayment',
            name='payment_method',
            field=models.CharField(max_length=16, choices=[('cashl', 'Cash (Indian)'), ('cashf', 'Cash (Foreign)'), ('cashd', 'Cash Deposit'), ('ccdcsl', 'Credit/Debit Card Swipe Local'), ('ccdcsf', 'Credit/Debit Card Swipe Foreign'), ('neftl', 'NEFT (Indian)'), ('neftf', 'NEFT (Foreign)'), ('chequel', 'Cheque (Indian)'), ('chequef', 'Cheque (Foreign)'), ('chequed', 'Cheque Deposit'), ('paypal', 'Paypal'), ('axis', 'Gateway Axis (Internet)'), ('treasury', 'ISKCON Treasury')], verbose_name='Payment Method'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contribution',
            name='payment_method',
            field=models.CharField(max_length=16, choices=[('cashl', 'Cash (Indian)'), ('cashf', 'Cash (Foreign)'), ('cashd', 'Cash Deposit'), ('ccdcsl', 'Credit/Debit Card Swipe Local'), ('ccdcsf', 'Credit/Debit Card Swipe Foreign'), ('neftl', 'NEFT (Indian)'), ('neftf', 'NEFT (Foreign)'), ('chequel', 'Cheque (Indian)'), ('chequef', 'Cheque (Foreign)'), ('chequed', 'Cheque Deposit'), ('paypal', 'Paypal'), ('axis', 'Gateway Axis (Internet)'), ('treasury', 'ISKCON Treasury')], verbose_name='Payment Method'),
            preserve_default=True,
        ),
    ]
