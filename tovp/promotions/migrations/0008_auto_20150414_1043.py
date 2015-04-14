# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0007_auto_20150405_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goldenbrick',
            name='name_on_brick',
            field=models.TextField(blank=True, max_length=100, help_text='Enter name which will be on the brick. Maximum 36 characters.', verbose_name='Name on the brick'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guruparamparabrick',
            name='name_on_brick',
            field=models.TextField(blank=True, max_length=100, help_text='Enter name which will be on the brick. Maximum 36 characters.', verbose_name='Name on the brick'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='nrsimhatile',
            name='name_on_brick',
            field=models.TextField(blank=True, max_length=100, help_text='Enter name which will be on the brick. Maximum 36 characters.', verbose_name='Name on the brick'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='radhamadhavabrick',
            name='name_on_brick',
            field=models.TextField(blank=True, max_length=100, help_text='Enter name which will be on the brick. Maximum 36 characters.', verbose_name='Name on the brick'),
            preserve_default=True,
        ),
    ]
