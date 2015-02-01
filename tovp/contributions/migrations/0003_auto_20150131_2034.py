# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0002_auto_20150131_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribution',
            name='bank',
            field=models.CharField(verbose_name='Bank', help_text='Write bank name (and possible branch or location) for cheque', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contribution',
            name='cleared_on',
            field=models.DateField(verbose_name='Cleared On', help_text='Enter date when transaction was completed (money came to TOVP)', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contribution',
            name='dated',
            field=models.DateField(verbose_name='Dated', help_text='Enter date on the cheque', null=True, blank=True),
            preserve_default=True,
        ),
    ]
