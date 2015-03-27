# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_auto_20150306_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='old_database_id',
            field=models.IntegerField(null=True, verbose_name='Old Database ID', blank=True, help_text='If you are transfering data from old database (CiviCRM), enter contact_id here. Otherwise leave empty.'),
            preserve_default=True,
        ),
    ]
