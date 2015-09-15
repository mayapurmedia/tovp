# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import audit_log.models.fields
import django.utils.timezone
import attachments.models
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(null=True, editable=False, max_length=40)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(null=True, editable=False, max_length=40)),
                ('object_id', models.PositiveIntegerField()),
                ('attachment_file', models.FileField(verbose_name='attachment', upload_to=attachments.models.Attachment.attachment_upload)),
                ('description', models.CharField(max_length=255)),
                ('attachment_type', models.CharField(max_length=100, verbose_name='Attachment Type', choices=[('passport', 'Passport'), ('cheque', 'Cheque'), ('other', 'Other Document')])),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('created_by', audit_log.models.fields.CreatingUserField(null=True, related_name='created_attachments_attachment_set', editable=False, verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', audit_log.models.fields.LastUserField(null=True, related_name='modified_attachments_attachment_set', editable=False, verbose_name='modified by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('delete_foreign_attachments', 'Can delete foreign attachments'),),
            },
            bases=(models.Model,),
        ),
    ]
