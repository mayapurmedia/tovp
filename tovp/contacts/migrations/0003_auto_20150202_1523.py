# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20150202_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='indian_address',
        ),
        migrations.RemoveField(
            model_name='person',
            name='indian_name',
        ),
    ]
