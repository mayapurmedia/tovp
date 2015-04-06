# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='signature',
            field=models.FileField(verbose_name='Digital Signature', upload_to='signatures', blank=True),
            preserve_default=True,
        ),
    ]
