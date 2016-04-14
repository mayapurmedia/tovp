# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0052_auto_20160413_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='receipt_type',
            field=models.CharField(choices=[('mayapur-receipt', 'Mayapur Receipt'), ('usa-receipt', 'USA Receipt'), ('external-receipt', 'External / Non Receipt')], max_length=100, default='mayapur-receipt', verbose_name='Receipt Type'),
        ),
    ]
