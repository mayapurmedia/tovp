# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0028_auto_20150504_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulkpayment',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed'), ('canceled', 'Canceled')], max_length=30, verbose_name='Status'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contribution',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed'), ('canceled', 'Canceled')], max_length=30, verbose_name='Status'),
            preserve_default=True,
        ),
    ]
