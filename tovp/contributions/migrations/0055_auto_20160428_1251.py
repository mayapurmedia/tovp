# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0054_auto_20160419_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='receipt_type',
            field=models.CharField(verbose_name='Receipt Type', choices=[('mayapur-receipt', 'Mayapur Receipt'), ('usa-receipt', 'USA Receipt'), ('external-receipt', 'External / Non Receipt')], default='external-receipt', max_length=100),
        ),
    ]
