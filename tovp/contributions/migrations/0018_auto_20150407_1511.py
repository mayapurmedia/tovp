# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0017_auto_20150406_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='source',
            field=models.CharField(verbose_name='Source', choices=[('nityananda', 'Nityananda Tour'), ('jps-office', 'JPS Office'), ('namahatta', 'JPS Namahatta'), ('jps-others', 'JPS Others'), ('nvs', 'Nava Yogendra Swami'), ('mso', 'MSO'), ('lm-reception', 'Life Membership Reception'), ('vrindavan-booth', 'Vrindavan Booth'), ('prabhupada-currency-inr', 'Prabhupada Currency INR'), ('other', 'Other')], blank=True, max_length=30, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pledge',
            name='source',
            field=models.CharField(verbose_name='Source', choices=[('nityananda', 'Nityananda Tour'), ('jps-office', 'JPS Office'), ('namahatta', 'JPS Namahatta'), ('jps-others', 'JPS Others'), ('nvs', 'Nava Yogendra Swami'), ('mso', 'MSO'), ('lm-reception', 'Life Membership Reception'), ('vrindavan-booth', 'Vrindavan Booth'), ('prabhupada-currency-inr', 'Prabhupada Currency INR'), ('other', 'Other')], blank=True, max_length=30, default=''),
            preserve_default=True,
        ),
    ]
