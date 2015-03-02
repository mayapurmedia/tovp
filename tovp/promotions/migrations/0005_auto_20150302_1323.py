# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0004_auto_20150302_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='goldenbrick',
            name='brick_status',
            field=models.CharField(verbose_name='Brick Status', max_length=100, default='need_to_send', choices=[('need_to_send', 'Need to send to DC'), ('name_given', 'Name given to DC'), ('brick_made', 'Brick is made')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='guruparamparabrick',
            name='brick_status',
            field=models.CharField(verbose_name='Brick Status', max_length=100, default='need_to_send', choices=[('need_to_send', 'Need to send to DC'), ('name_given', 'Name given to DC'), ('brick_made', 'Brick is made')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nrsimhatile',
            name='brick_status',
            field=models.CharField(verbose_name='Brick Status', max_length=100, default='need_to_send', choices=[('need_to_send', 'Need to send to DC'), ('name_given', 'Name given to DC'), ('brick_made', 'Brick is made')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='radhamadhavabrick',
            name='brick_status',
            field=models.CharField(verbose_name='Brick Status', max_length=100, default='need_to_send', choices=[('need_to_send', 'Need to send to DC'), ('name_given', 'Name given to DC'), ('brick_made', 'Brick is made')]),
            preserve_default=True,
        ),
    ]
