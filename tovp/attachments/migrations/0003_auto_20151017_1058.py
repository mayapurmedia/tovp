# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0002_auto_20150916_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='attachment_type',
            field=models.CharField(verbose_name='Attachment Type', choices=[('passport', 'Passport'), ('cheque', 'Cheque'), ('other', 'Other Document')], max_length=50),
            preserve_default=True,
        ),
    ]
