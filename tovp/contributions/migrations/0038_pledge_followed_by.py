# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contributions', '0037_auto_20151017_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledge',
            name='followed_by',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True, related_name='pledges'),
            preserve_default=True,
        ),
    ]
