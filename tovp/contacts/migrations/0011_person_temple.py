# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0010_auto_20150511_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='temple',
            field=models.CharField(max_length=100, help_text='If person tells you association with temple, please enter it here.', blank=True),
            preserve_default=True,
        ),
    ]
