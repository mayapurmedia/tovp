# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0030_auto_20150514_1332'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contribution',
            options={'permissions': (('can_edit_completed', 'Can edit completed'), ('can_change_deposit_status', 'Can change deposit status'), ('can_deposit', 'Can mark as deposited'))},
        ),
    ]
