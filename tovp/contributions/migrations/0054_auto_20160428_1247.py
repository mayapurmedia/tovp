# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0053_auto_20160414_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='receipt_type',
            field=models.CharField(choices=[('mayapur-receipt', 'Mayapur Receipt'), ('usa-receipt', 'USA Receipt'), ('external-receipt', 'External / Non Receipt')], max_length=100, verbose_name='Receipt Type', default='external-receipt'),
        ),
    ]
