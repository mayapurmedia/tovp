# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20150202_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='yatra',
            field=models.CharField(choices=[('middle-east', 'Middle East'), ('russia', 'Russia')], blank=True, help_text='If person belongs to one the of yatras in drowpdown, please choose it', null=True, verbose_name='Yatra', max_length=100),
            preserve_default=True,
        ),
    ]
