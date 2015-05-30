# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0029_auto_20150514_1331'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contribution',
            options={'permissions': (('can_edit_completed', 'Can edit completed'), ('can_deposit', 'Can deposit'))},
        ),
        migrations.AddField(
            model_name='contribution',
            name='deposited_status',
            field=models.CharField(choices=[('not-deposited', 'Not deposited'), ('ready-to-deposit', 'Ready to deposit'), ('deposited', 'Deposited')], verbose_name='Is Deposited', default='not-deposited', max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contribution',
            name='deposited_status_changed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='deposited_status'),
            preserve_default=True,
        ),
    ]
