# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0027_auto_20150504_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledge',
            name='status',
            field=models.CharField(verbose_name='Status', default='pending', blank=True, choices=[('pending', 'Pledged'), ('partial', 'Partially Paid'), ('completed', 'Completed'), ('failed', 'Shadow'), ('canceled', 'Canceled')], max_length=30),
            preserve_default=True,
        ),
    ]
