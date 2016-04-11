# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def set_receipt_types(apps, schema_editor):
    Contribution = apps.get_model("contributions", "Contribution")
    for contribution in Contribution.objects.all():
        if not contribution.receipt_type:
            if contribution.is_external:
                contribution.receipt_type = 'external-receipt'
            else:
                contribution.receipt_type = 'mayapur-receipt'
            contribution.save()


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0049_contribution_receipt_type'),
    ]

    operations = [
        migrations.RunPython(set_receipt_types),
    ]
