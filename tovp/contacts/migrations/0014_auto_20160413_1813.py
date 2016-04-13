# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0013_auto_20160302_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='note',
            field=models.TextField(blank=True, verbose_name='Note'),
        ),
    ]
