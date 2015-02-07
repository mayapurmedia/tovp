# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goldcoin',
            name='certificate_given',
            field=models.BooleanField(help_text='Has certificate for this promotion been given?', db_index=True, default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goldcoin',
            name='certificate_given_date',
            field=model_utils.fields.MonitorField(monitor='certificate_given', default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goldcoin',
            name='coin_given',
            field=models.BooleanField(help_text='Has coin for this promotion been given?', db_index=True, default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goldcoin',
            name='coin_given_date',
            field=model_utils.fields.MonitorField(monitor='coin_given', default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goldenbrick',
            name='certificate_given',
            field=models.BooleanField(help_text='Has certificate for this promotion been given?', db_index=True, default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goldenbrick',
            name='certificate_given_date',
            field=model_utils.fields.MonitorField(monitor='certificate_given', default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goldenbrick',
            name='coin_given',
            field=models.BooleanField(help_text='Has coin for this promotion been given?', db_index=True, default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goldenbrick',
            name='coin_given_date',
            field=model_utils.fields.MonitorField(monitor='coin_given', default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nrsimhatile',
            name='certificate_given',
            field=models.BooleanField(help_text='Has certificate for this promotion been given?', db_index=True, default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nrsimhatile',
            name='certificate_given_date',
            field=model_utils.fields.MonitorField(monitor='certificate_given', default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nrsimhatile',
            name='coin_given',
            field=models.BooleanField(help_text='Has coin for this promotion been given?', db_index=True, default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nrsimhatile',
            name='coin_given_date',
            field=model_utils.fields.MonitorField(monitor='coin_given', default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='platinumcoin',
            name='certificate_given',
            field=models.BooleanField(help_text='Has certificate for this promotion been given?', db_index=True, default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='platinumcoin',
            name='certificate_given_date',
            field=model_utils.fields.MonitorField(monitor='certificate_given', default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='platinumcoin',
            name='coin_given',
            field=models.BooleanField(help_text='Has coin for this promotion been given?', db_index=True, default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='platinumcoin',
            name='coin_given_date',
            field=model_utils.fields.MonitorField(monitor='coin_given', default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='radhamadhavabrick',
            name='certificate_given',
            field=models.BooleanField(help_text='Has certificate for this promotion been given?', db_index=True, default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='radhamadhavabrick',
            name='certificate_given_date',
            field=model_utils.fields.MonitorField(monitor='certificate_given', default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='radhamadhavabrick',
            name='coin_given',
            field=models.BooleanField(help_text='Has coin for this promotion been given?', db_index=True, default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='radhamadhavabrick',
            name='coin_given_date',
            field=model_utils.fields.MonitorField(monitor='coin_given', default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='silvercoin',
            name='certificate_given',
            field=models.BooleanField(help_text='Has certificate for this promotion been given?', db_index=True, default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='silvercoin',
            name='certificate_given_date',
            field=model_utils.fields.MonitorField(monitor='certificate_given', default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='silvercoin',
            name='coin_given',
            field=models.BooleanField(help_text='Has coin for this promotion been given?', db_index=True, default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='silvercoin',
            name='coin_given_date',
            field=model_utils.fields.MonitorField(monitor='coin_given', default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='squarefeet',
            name='certificate_given',
            field=models.BooleanField(help_text='Has certificate for this promotion been given?', db_index=True, default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='squarefeet',
            name='certificate_given_date',
            field=model_utils.fields.MonitorField(monitor='certificate_given', default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='squaremeter',
            name='certificate_given',
            field=models.BooleanField(help_text='Has certificate for this promotion been given?', db_index=True, default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='squaremeter',
            name='certificate_given_date',
            field=model_utils.fields.MonitorField(monitor='certificate_given', default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
