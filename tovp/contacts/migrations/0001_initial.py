# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(choices=[('Mr', 'Mr'), ('Miss', 'Miss'), ('Mrs', 'Mrs'), ('Ms', 'Ms'), ('Dr', 'Dr')], verbose_name='Title', max_length=64, blank=True)),
                ('first_name', models.CharField(max_length=100, help_text='Enter your first name.')),
                ('middle_name', models.CharField(blank=True, max_length=100, help_text='Enter your middle name.')),
                ('last_name', models.CharField(max_length=100, help_text='Enter your surname.')),
                ('initiated_name', models.CharField(blank=True, max_length=100, help_text='Spiritual name if you have e.g: Krishna Das, Tulasi Dasi, Bhakta Burfi')),
                ('email', models.EmailField(verbose_name='Email', max_length=200, blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=100, help_text='Enter your phone number. If it is a non-Indian number please use the international format e.g.: +421 222 333 444')),
                ('address', models.TextField(verbose_name='Address', max_length=255, blank=True)),
                ('city', models.CharField(verbose_name='City', max_length=255, blank=True)),
                ('state', models.CharField(verbose_name='State/County', max_length=255, blank=True)),
                ('postcode', models.CharField(verbose_name='Post/Zip-code', max_length=64, blank=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('pan_card_number', models.CharField(null=True, verbose_name='PAN card number', max_length=50, blank=True, help_text='Required for Indian citizens. Enter your PAN card number.')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
