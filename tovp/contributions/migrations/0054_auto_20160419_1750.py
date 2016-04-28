# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0053_auto_20160414_1136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contribution',
            options={'permissions': (('can_edit_completed', 'Can edit completed'), ('can_change_deposit_status', 'Can change deposit status'), ('can_do_follow_up', 'Can do follow up'), ('can_deposit', 'Can mark as deposited'), ('can_move_contribution', 'Can move contribution'))},
        ),
    ]
