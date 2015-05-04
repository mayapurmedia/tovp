# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0026_auto_20150420_1746'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contribution',
            options={'permissions': (('can_edit_completed', 'Can edit completed'),)},
        ),
    ]
