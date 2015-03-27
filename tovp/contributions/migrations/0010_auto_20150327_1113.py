# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def set_receipt_date(apps, schema_editor):
    Contribution = apps.get_model("contributions", "Contribution")
    for contribution in Contribution.objects.all():
        contribution.save(update_fields=["receipt_date"])


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0009_auto_20150306_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribution',
            name='receipt_date',
            field=models.DateField(help_text='Enter date which should be on the receipt.', blank=True, verbose_name='Receipt Date', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contribution',
            name='serial_number',
            field=models.CharField(help_text='Serial Number of this contribution for financial year.', blank=True, verbose_name='Serial Number', max_length=5),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contribution',
            name='serial_year',
            field=models.CharField(help_text='Serial Number Year of this contribution.', blank=True, verbose_name='Serial Number Year', max_length=5),
            preserve_default=True,
        ),
        migrations.RunPython(set_receipt_date),
    ]
