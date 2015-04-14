# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0008_auto_20150405_1214'),
        ('contributions', '0020_bulkpayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribution',
            name='bulk_payment',
            field=models.ForeignKey(null=True, help_text='If this contribution is part of bulk payment please chooseit here.', to='contributions.BulkPayment', blank=True, related_name='contributions', verbose_name='Bulk Payment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contribution',
            name='collector',
            field=models.ForeignKey(null=True, help_text='If this is comes through collector.', to='contacts.Person', blank=True, related_name='collector_contributions', verbose_name='Collector'),
            preserve_default=True,
        ),
    ]
