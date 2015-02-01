# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0003_auto_20150131_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribution',
            name='book_number',
            field=models.CharField(help_text='Enter if you are entering contribution from book', verbose_name='Book Number', blank=True, max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contribution',
            name='slip_number',
            field=models.CharField(help_text='Enter if you are entering contribution from slip', verbose_name='Slip Number', blank=True, max_length=20),
            preserve_default=True,
        ),
    ]
