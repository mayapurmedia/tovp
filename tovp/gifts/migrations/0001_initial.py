# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import audit_log.models.fields
import ananta.models
import model_utils.fields
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0012_person_note'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(null=True, editable=False, max_length=40)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(null=True, editable=False, max_length=40)),
                ('name', models.CharField(help_text='Enter gift name.', max_length=100)),
                ('description', models.TextField(blank=True)),
                ('created_by', audit_log.models.fields.CreatingUserField(null=True, to=settings.AUTH_USER_MODEL, related_name='created_gifts_gift_set', editable=False, verbose_name='created by')),
                ('modified_by', audit_log.models.fields.LastUserField(null=True, to=settings.AUTH_USER_MODEL, related_name='modified_gifts_gift_set', editable=False, verbose_name='modified by')),
            ],
            options={
                'abstract': False,
            },
            bases=(ananta.models.NextPrevMixin, models.Model),
        ),
        migrations.CreateModel(
            name='GiftGiven',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(null=True, editable=False, max_length=40)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(null=True, editable=False, max_length=40)),
                ('status', model_utils.fields.StatusField(choices=[('sent', 'Sent'), ('returned', 'Returned'), ('delivered', 'Delivered')], default='sent', no_check_for_status=True, max_length=100)),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status')),
                ('note', models.TextField(verbose_name='Note', blank=True)),
                ('created_by', audit_log.models.fields.CreatingUserField(null=True, to=settings.AUTH_USER_MODEL, related_name='created_gifts_giftgiven_set', editable=False, verbose_name='created by')),
                ('gift', models.ForeignKey(to='gifts.Gift', related_name='gifts', verbose_name='Gift')),
                ('modified_by', audit_log.models.fields.LastUserField(null=True, to=settings.AUTH_USER_MODEL, related_name='modified_gifts_giftgiven_set', editable=False, verbose_name='modified by')),
                ('person', models.ForeignKey(to='contacts.Person', related_name='gifts', verbose_name='Person')),
            ],
            options={
                'abstract': False,
            },
            bases=(ananta.models.NextPrevMixin, models.Model),
        ),
    ]
