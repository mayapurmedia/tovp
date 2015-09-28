# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0034_auto_20150913_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulkpayment',
            name='source',
            field=models.CharField(default='', verbose_name='Source', choices=[('nityananda', 'Nityananda Tour'), ('jps-office', 'JPS Office'), ('namahatta', 'JPS Namahatta'), ('jps-others', 'JPS Others'), ('gkg-vp-2015', 'GKG Vyasa Puja 2015'), ('bcs-vp-2015', 'BCS Vyasa Puja 2015'), ('kanjurmarg-mumbai-2015', 'Kanjurmarg Mumbai 2015'), ('nvs', 'Nava Yogendra Swami'), ('mso', 'MSO'), ('lm-reception', 'Life Membership Reception'), ('vrindavan-booth', 'Vrindavan Booth'), ('prabhupada-currency-inr', 'Prabhupada Currency INR'), ('other', 'Other')], blank=True, max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contribution',
            name='source',
            field=models.CharField(default='', verbose_name='Source', choices=[('nityananda', 'Nityananda Tour'), ('jps-office', 'JPS Office'), ('namahatta', 'JPS Namahatta'), ('jps-others', 'JPS Others'), ('gkg-vp-2015', 'GKG Vyasa Puja 2015'), ('bcs-vp-2015', 'BCS Vyasa Puja 2015'), ('kanjurmarg-mumbai-2015', 'Kanjurmarg Mumbai 2015'), ('nvs', 'Nava Yogendra Swami'), ('mso', 'MSO'), ('lm-reception', 'Life Membership Reception'), ('vrindavan-booth', 'Vrindavan Booth'), ('prabhupada-currency-inr', 'Prabhupada Currency INR'), ('other', 'Other')], blank=True, max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pledge',
            name='source',
            field=models.CharField(default='', verbose_name='Source', choices=[('nityananda', 'Nityananda Tour'), ('jps-office', 'JPS Office'), ('namahatta', 'JPS Namahatta'), ('jps-others', 'JPS Others'), ('gkg-vp-2015', 'GKG Vyasa Puja 2015'), ('bcs-vp-2015', 'BCS Vyasa Puja 2015'), ('kanjurmarg-mumbai-2015', 'Kanjurmarg Mumbai 2015'), ('nvs', 'Nava Yogendra Swami'), ('mso', 'MSO'), ('lm-reception', 'Life Membership Reception'), ('vrindavan-booth', 'Vrindavan Booth'), ('prabhupada-currency-inr', 'Prabhupada Currency INR'), ('other', 'Other')], blank=True, max_length=30),
            preserve_default=True,
        ),
    ]
