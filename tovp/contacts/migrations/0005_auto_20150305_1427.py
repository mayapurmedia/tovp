# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_person_yatra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(blank=True, help_text='Enter your first name.', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(blank=True, help_text='Enter your surname.', max_length=100),
            preserve_default=True,
        ),
    ]
