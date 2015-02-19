# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0008_auto_20150219_1555'),
        ('promotions', '0002_auto_20150207_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuruParamparaBrick',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('certificate_given', models.BooleanField(db_index=True, help_text='Has certificate for this promotion been given?', default=False)),
                ('certificate_given_date', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='certificate_given')),
                ('coin_given', models.BooleanField(db_index=True, help_text='Has coin for this promotion been given?', default=False)),
                ('coin_given_date', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='coin_given')),
                ('name_on_brick', models.TextField(help_text='Enter name which will be on the brick. Maximum 100 characters.', max_length=100, blank=True, verbose_name='Name on the brick')),
                ('pledge', models.ForeignKey(to='contributions.Pledge', related_name='+', verbose_name='Pledge')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
