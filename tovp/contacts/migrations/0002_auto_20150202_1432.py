# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='indian_address',
            field=models.CharField(max_length=255, blank=True, verbose_name='Indian Address'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='indian_name',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
