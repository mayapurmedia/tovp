# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_signature'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='only_external_receipts',
            field=models.BooleanField(help_text='If checked everything user creates will have external receipt.was given.', db_index=True, verbose_name='Non Mayapur TOVP receipt', default=False),
            preserve_default=True,
        ),
    ]
