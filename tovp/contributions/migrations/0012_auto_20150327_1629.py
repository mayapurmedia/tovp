# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0011_auto_20150327_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='payment_method',
            field=models.CharField(verbose_name='Payment Method', max_length=16, choices=[('cashl', 'Cash (Indian)'), ('cashf', 'Cash (Foreign)'), ('ccdcsl', 'Credit/Debit Card Swipe Local'), ('ccdcsf', 'Credit/Debit Card Swipe Foreign'), ('neftl', 'NEFT (Indian)'), ('neftf', 'NEFT (Foreign)'), ('chequel', 'Cheque (Indian)'), ('chequef', 'Cheque (Foreign)'), ('paypal', 'Paypal'), ('axis', 'Gateway Axis (Internet)')]),
            preserve_default=True,
        ),
    ]
