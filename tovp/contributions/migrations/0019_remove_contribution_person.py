# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0018_auto_20150407_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contribution',
            name='person',
        ),
    ]
