# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0048_auto_20160323_0545'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribution',
            name='receipt_type',
            field=models.CharField(verbose_name='Receipt Type', blank=True, choices=[('mayapur-receipt', 'Mayapur Receipt'), ('usa-receipt', 'USA Receipt'), ('external-receipt', 'External / Non Receipt')], max_length=100),
        ),
    ]
