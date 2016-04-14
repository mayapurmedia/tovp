# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20151205_0549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='only_external_receipts',
        ),
        migrations.AddField(
            model_name='user',
            name='default_usa_receipt',
            field=models.BooleanField(help_text='If checked USA receipt will be selected as default', db_index=True, default=False, verbose_name='USA receipt by default'),
        ),
    ]
