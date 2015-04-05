# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
import audit_log.models.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('promotions', '0006_generaldonation'),
    ]

    operations = [
        migrations.AddField(
            model_name='generaldonation',
            name='created_by',
            field=audit_log.models.fields.CreatingUserField(editable=False, related_name='created_promotions_generaldonation_set', verbose_name='created by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='generaldonation',
            name='created_with_session_key',
            field=audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='generaldonation',
            name='modified_by',
            field=audit_log.models.fields.LastUserField(editable=False, related_name='modified_promotions_generaldonation_set', verbose_name='modified by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='generaldonation',
            name='modified_with_session_key',
            field=audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goldcoin',
            name='created_by',
            field=audit_log.models.fields.CreatingUserField(editable=False, related_name='created_promotions_goldcoin_set', verbose_name='created by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goldcoin',
            name='created_with_session_key',
            field=audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goldcoin',
            name='modified_by',
            field=audit_log.models.fields.LastUserField(editable=False, related_name='modified_promotions_goldcoin_set', verbose_name='modified by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goldcoin',
            name='modified_with_session_key',
            field=audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goldenbrick',
            name='created_by',
            field=audit_log.models.fields.CreatingUserField(editable=False, related_name='created_promotions_goldenbrick_set', verbose_name='created by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goldenbrick',
            name='created_with_session_key',
            field=audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goldenbrick',
            name='modified_by',
            field=audit_log.models.fields.LastUserField(editable=False, related_name='modified_promotions_goldenbrick_set', verbose_name='modified by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goldenbrick',
            name='modified_with_session_key',
            field=audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='guruparamparabrick',
            name='created_by',
            field=audit_log.models.fields.CreatingUserField(editable=False, related_name='created_promotions_guruparamparabrick_set', verbose_name='created by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='guruparamparabrick',
            name='created_with_session_key',
            field=audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='guruparamparabrick',
            name='modified_by',
            field=audit_log.models.fields.LastUserField(editable=False, related_name='modified_promotions_guruparamparabrick_set', verbose_name='modified by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='guruparamparabrick',
            name='modified_with_session_key',
            field=audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nrsimhatile',
            name='created_by',
            field=audit_log.models.fields.CreatingUserField(editable=False, related_name='created_promotions_nrsimhatile_set', verbose_name='created by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nrsimhatile',
            name='created_with_session_key',
            field=audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nrsimhatile',
            name='modified_by',
            field=audit_log.models.fields.LastUserField(editable=False, related_name='modified_promotions_nrsimhatile_set', verbose_name='modified by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nrsimhatile',
            name='modified_with_session_key',
            field=audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='platinumcoin',
            name='created_by',
            field=audit_log.models.fields.CreatingUserField(editable=False, related_name='created_promotions_platinumcoin_set', verbose_name='created by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='platinumcoin',
            name='created_with_session_key',
            field=audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='platinumcoin',
            name='modified_by',
            field=audit_log.models.fields.LastUserField(editable=False, related_name='modified_promotions_platinumcoin_set', verbose_name='modified by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='platinumcoin',
            name='modified_with_session_key',
            field=audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='radhamadhavabrick',
            name='created_by',
            field=audit_log.models.fields.CreatingUserField(editable=False, related_name='created_promotions_radhamadhavabrick_set', verbose_name='created by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='radhamadhavabrick',
            name='created_with_session_key',
            field=audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='radhamadhavabrick',
            name='modified_by',
            field=audit_log.models.fields.LastUserField(editable=False, related_name='modified_promotions_radhamadhavabrick_set', verbose_name='modified by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='radhamadhavabrick',
            name='modified_with_session_key',
            field=audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='silvercoin',
            name='created_by',
            field=audit_log.models.fields.CreatingUserField(editable=False, related_name='created_promotions_silvercoin_set', verbose_name='created by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='silvercoin',
            name='created_with_session_key',
            field=audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='silvercoin',
            name='modified_by',
            field=audit_log.models.fields.LastUserField(editable=False, related_name='modified_promotions_silvercoin_set', verbose_name='modified by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='silvercoin',
            name='modified_with_session_key',
            field=audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='squarefeet',
            name='created_by',
            field=audit_log.models.fields.CreatingUserField(editable=False, related_name='created_promotions_squarefeet_set', verbose_name='created by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='squarefeet',
            name='created_with_session_key',
            field=audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='squarefeet',
            name='modified_by',
            field=audit_log.models.fields.LastUserField(editable=False, related_name='modified_promotions_squarefeet_set', verbose_name='modified by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='squarefeet',
            name='modified_with_session_key',
            field=audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='squaremeter',
            name='created_by',
            field=audit_log.models.fields.CreatingUserField(editable=False, related_name='created_promotions_squaremeter_set', verbose_name='created by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='squaremeter',
            name='created_with_session_key',
            field=audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='squaremeter',
            name='modified_by',
            field=audit_log.models.fields.LastUserField(editable=False, related_name='modified_promotions_squaremeter_set', verbose_name='modified by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='squaremeter',
            name='modified_with_session_key',
            field=audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='trustee',
            name='created_by',
            field=audit_log.models.fields.CreatingUserField(editable=False, related_name='created_promotions_trustee_set', verbose_name='created by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='trustee',
            name='created_with_session_key',
            field=audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='trustee',
            name='modified_by',
            field=audit_log.models.fields.LastUserField(editable=False, related_name='modified_promotions_trustee_set', verbose_name='modified by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='trustee',
            name='modified_with_session_key',
            field=audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False),
            preserve_default=True,
        ),
    ]
