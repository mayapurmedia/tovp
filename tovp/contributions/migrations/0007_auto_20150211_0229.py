# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import audit_log.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contributions', '0006_auto_20150209_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribution',
            name='created_by',
            field=audit_log.models.fields.CreatingUserField(verbose_name='created by', to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='created_contributions_contribution_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contribution',
            name='created_with_session_key',
            field=audit_log.models.fields.CreatingSessionKeyField(null=True, editable=False, max_length=40),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contribution',
            name='modified_by',
            field=audit_log.models.fields.LastUserField(verbose_name='modified by', to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='modified_contributions_contribution_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contribution',
            name='modified_with_session_key',
            field=audit_log.models.fields.LastSessionKeyField(null=True, editable=False, max_length=40),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pledge',
            name='created_by',
            field=audit_log.models.fields.CreatingUserField(verbose_name='created by', to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='created_contributions_pledge_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pledge',
            name='created_with_session_key',
            field=audit_log.models.fields.CreatingSessionKeyField(null=True, editable=False, max_length=40),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pledge',
            name='modified_by',
            field=audit_log.models.fields.LastUserField(verbose_name='modified by', to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='modified_contributions_pledge_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pledge',
            name='modified_with_session_key',
            field=audit_log.models.fields.LastSessionKeyField(null=True, editable=False, max_length=40),
            preserve_default=True,
        ),
    ]
