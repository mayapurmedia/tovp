# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20150305_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='yatra',
            field=models.CharField(blank=True, max_length=100, verbose_name='Yatra', help_text='If person belongs to one the of yatras in drowpdown, please choose it', choices=[('middle-east', 'Middle East'), ('north-america', 'North America'), ('russia', 'Russia'), ('south-africa', 'South Africa'), ('uk', 'UK')], null=True),
            preserve_default=True,
        ),
    ]
