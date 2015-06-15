# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields
import audit_log.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contributions', '0032_auto_20150609_1721'),
        ('promotions', '0008_auto_20150414_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvaitaCoin',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(editable=False, max_length=40, null=True)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(editable=False, max_length=40, null=True)),
                ('certificate_given', models.BooleanField(default=False, db_index=True, help_text='Has certificate for this promotion been given?')),
                ('certificate_given_date', model_utils.fields.MonitorField(monitor='certificate_given', default=django.utils.timezone.now)),
                ('coin_given', models.BooleanField(default=False, db_index=True, help_text='Has coin for this promotion been given?')),
                ('coin_given_date', model_utils.fields.MonitorField(monitor='coin_given', default=django.utils.timezone.now)),
                ('created_by', audit_log.models.fields.CreatingUserField(to=settings.AUTH_USER_MODEL, verbose_name='created by', editable=False, related_name='created_promotions_advaitacoin_set', null=True)),
                ('modified_by', audit_log.models.fields.LastUserField(to=settings.AUTH_USER_MODEL, verbose_name='modified by', editable=False, related_name='modified_promotions_advaitacoin_set', null=True)),
                ('pledge', models.ForeignKey(to='contributions.Pledge', verbose_name='Pledge', related_name='+')),
            ],
            options={
                'verbose_name': 'Advaita Coin',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GadadharCoin',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(editable=False, max_length=40, null=True)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(editable=False, max_length=40, null=True)),
                ('certificate_given', models.BooleanField(default=False, db_index=True, help_text='Has certificate for this promotion been given?')),
                ('certificate_given_date', model_utils.fields.MonitorField(monitor='certificate_given', default=django.utils.timezone.now)),
                ('coin_given', models.BooleanField(default=False, db_index=True, help_text='Has coin for this promotion been given?')),
                ('coin_given_date', model_utils.fields.MonitorField(monitor='coin_given', default=django.utils.timezone.now)),
                ('created_by', audit_log.models.fields.CreatingUserField(to=settings.AUTH_USER_MODEL, verbose_name='created by', editable=False, related_name='created_promotions_gadadharcoin_set', null=True)),
                ('modified_by', audit_log.models.fields.LastUserField(to=settings.AUTH_USER_MODEL, verbose_name='modified by', editable=False, related_name='modified_promotions_gadadharcoin_set', null=True)),
                ('pledge', models.ForeignKey(to='contributions.Pledge', verbose_name='Pledge', related_name='+')),
            ],
            options={
                'verbose_name': 'Gadadhar Coin',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RadharaniCoin',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(editable=False, max_length=40, null=True)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(editable=False, max_length=40, null=True)),
                ('certificate_given', models.BooleanField(default=False, db_index=True, help_text='Has certificate for this promotion been given?')),
                ('certificate_given_date', model_utils.fields.MonitorField(monitor='certificate_given', default=django.utils.timezone.now)),
                ('coin_given', models.BooleanField(default=False, db_index=True, help_text='Has coin for this promotion been given?')),
                ('coin_given_date', model_utils.fields.MonitorField(monitor='coin_given', default=django.utils.timezone.now)),
                ('created_by', audit_log.models.fields.CreatingUserField(to=settings.AUTH_USER_MODEL, verbose_name='created by', editable=False, related_name='created_promotions_radharanicoin_set', null=True)),
                ('modified_by', audit_log.models.fields.LastUserField(to=settings.AUTH_USER_MODEL, verbose_name='modified by', editable=False, related_name='modified_promotions_radharanicoin_set', null=True)),
                ('pledge', models.ForeignKey(to='contributions.Pledge', verbose_name='Pledge', related_name='+')),
            ],
            options={
                'verbose_name': 'Radharani Coin',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='goldcoin',
            options={'verbose_name': 'Nityananda Coin'},
        ),
        migrations.AlterModelOptions(
            name='platinumcoin',
            options={'verbose_name': 'Caitanya Coin'},
        ),
        migrations.AlterModelOptions(
            name='silvercoin',
            options={'verbose_name': 'Srivas Coin'},
        ),
    ]
