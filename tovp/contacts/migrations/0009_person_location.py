# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0008_auto_20150405_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='location',
            field=models.CharField(max_length=100, blank=True, verbose_name='Collection Location'),
            preserve_default=True,
        ),
    ]
