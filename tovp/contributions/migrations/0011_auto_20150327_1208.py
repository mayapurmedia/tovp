# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0010_auto_20150327_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='payment_method',
            field=models.CharField(verbose_name='Payment Method', choices=[('cashl', 'Cash (Indian)'), ('cashf', 'Cash (Foreign)'), ('ccdcsl', 'Credit/Debit Card Swipe Local'), ('ccdcsf', 'Credit/Debit Card Swipe Foreign'), ('neftl', 'NEFT (Indian)'), ('neftf', 'NEFT (Foreign)'), ('chequel', 'Cheque (Indian)'), ('chequef', 'Cheque (Foreign)'), ('paypal', 'Paypal')], max_length=16),
            preserve_default=True,
        ),
    ]
