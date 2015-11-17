# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import audit_log.models.fields
from django.conf import settings
import model_utils.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contributions', '0038_pledge_followed_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(editable=False, max_length=40, null=True)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(editable=False, max_length=40, null=True)),
                ('status', models.CharField(choices=[('wrong-contact', 'Wrong contact'), ('could-not-reach', 'Could not reach'), ('waiting-reply', 'Waiting for reply'), ('agreed-to-pay', 'Agreed to pay'), ('will-not-pay', 'Will not pay')], verbose_name='Status', max_length=30)),
                ('note', models.TextField(verbose_name='Note', blank=True)),
                ('created_by', audit_log.models.fields.CreatingUserField(editable=False, verbose_name='created by', to=settings.AUTH_USER_MODEL, related_name='created_contributions_followup_set', null=True)),
                ('modified_by', audit_log.models.fields.LastUserField(editable=False, verbose_name='modified by', to=settings.AUTH_USER_MODEL, related_name='modified_contributions_followup_set', null=True)),
                ('pledge', models.ForeignKey(related_name='follow_ups', verbose_name='Pledge', to='contributions.Pledge')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='contribution',
            options={'permissions': (('can_edit_completed', 'Can edit completed'), ('can_change_deposit_status', 'Can change deposit status'), ('can_do_follow_up', 'Can do follow up'), ('can_deposit', 'Can mark as deposited'))},
        ),
    ]
