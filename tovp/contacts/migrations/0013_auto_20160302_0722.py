# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0012_person_note'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'permissions': (('can_export', 'Can export'),)},
        ),
    ]
