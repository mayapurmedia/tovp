# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0005_auto_20150202_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='pledge',
            field=models.ForeignKey(related_name='contributions', to='contributions.Pledge', verbose_name='Pledge'),
            preserve_default=True,
        ),
    ]
