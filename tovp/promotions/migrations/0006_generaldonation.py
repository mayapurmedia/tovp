# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0008_auto_20150219_1555'),
        ('promotions', '0005_auto_20150302_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralDonation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('pledge', models.ForeignKey(verbose_name='Pledge', to='contributions.Pledge', related_name='+')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
