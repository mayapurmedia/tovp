# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0032_auto_20150609_1721'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pledge',
            options={'permissions': (('can_delete_if_no_contributions', 'Can delete if no contributions'),)},
        ),
    ]
