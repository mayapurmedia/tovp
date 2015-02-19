# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0007_auto_20150211_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledge',
            name='status',
            field=models.CharField(max_length=30, verbose_name='Status', default='pending', blank=True, choices=[('pending', 'Pledged'), ('partial', 'Partially Paid'), ('completed', 'Completed'), ('failed', 'Shadow')]),
            preserve_default=True,
        ),
    ]
