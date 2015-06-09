# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0011_person_temple'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='note',
            field=models.TextField(max_length=255, verbose_name='Note', blank=True),
            preserve_default=True,
        ),
    ]
