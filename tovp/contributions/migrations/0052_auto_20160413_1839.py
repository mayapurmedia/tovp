# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0051_auto_20160413_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='status',
            field=models.CharField(choices=[('wrong-contact', 'Wrong contact'), ('could-not-reach', 'Could not reach'), ('waiting-reply', 'Waiting for reply'), ('agreed-to-pay', 'Agreed to pay'), ('see-note', 'See note'), ('will-not-pay', 'Will not pay')], verbose_name='Status', max_length=30),
        ),
    ]
