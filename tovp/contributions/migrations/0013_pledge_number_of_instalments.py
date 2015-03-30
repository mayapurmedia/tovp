# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0012_auto_20150327_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledge',
            name='number_of_instalments',
            field=models.IntegerField(help_text='If somebody knows in how many instalment they would like to pay the pledge.', verbose_name='Number of instalments', default=1),
            preserve_default=True,
        ),
    ]
