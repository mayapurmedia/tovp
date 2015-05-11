# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0009_person_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='pan_card_number',
            field=models.CharField(blank=True, verbose_name='PAN card number', max_length=50, help_text='Required for Indian citizens. Enter your PAN card number.', null=True, validators=[django.core.validators.RegexValidator(code='invalid_pan_number', regex='[A-Za-z]{5}\\d{4}[A-Za-z]{1}', message='Seems like invalid PAN Card Number.')]),
            preserve_default=True,
        ),
    ]
