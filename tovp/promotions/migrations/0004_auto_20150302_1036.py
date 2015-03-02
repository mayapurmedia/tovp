# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0003_guruparamparabrick'),
    ]

    operations = [
        migrations.AddField(
            model_name='squarefeet',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='Quantity', default=1, help_text='Enter how many feets you want to add.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='squaremeter',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='Quantity', default=1, help_text='Enter how many meters you want to add.'),
            preserve_default=True,
        ),
    ]
