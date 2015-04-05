# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import audit_log.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0007_person_old_database_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='created_by',
            field=audit_log.models.fields.CreatingUserField(related_name='created_contacts_person_set', verbose_name='created by', null=True, to=settings.AUTH_USER_MODEL, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='created_with_session_key',
            field=audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='modified_by',
            field=audit_log.models.fields.LastUserField(related_name='modified_contacts_person_set', verbose_name='modified by', null=True, to=settings.AUTH_USER_MODEL, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='modified_with_session_key',
            field=audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False),
            preserve_default=True,
        ),
    ]
