# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0043_auto_20151127_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulkpayment',
            name='source',
            field=models.CharField(blank=True, max_length=30, default='', choices=[('tovp-f-mayapur', 'TOVP Fundraising Mayapur'), ('nityananda', 'Nityananda Tour'), ('jps-office', 'JPS Office'), ('namahatta', 'JPS Namahatta'), ('jps-others', 'JPS Others'), ('gkg-vp-2015', 'GKG Vyasa Puja 2015'), ('bcs-vp-2015', 'BCS Vyasa Puja 2015'), ('neel-vasan-das', 'Neel Vasan Das'), ('vvps-vp-2015', 'Vedavyasapriya Swami Vyasa Puja 2015'), ('rns-kartik-yatra', 'RNS Kartik Yatra'), ('j-w-marriot', 'J W Marriot'), ('kanjurmarg-mumbai-2015', 'Kanjurmarg Mumbai 2015'), ('nvs', 'Nava Yogendra Swami'), ('mso', 'MSO'), ('lm-reception', 'Life Membership Reception'), ('vrindavan-booth', 'Vrindavan Booth'), ('prabhupada-currency-inr', 'Prabhupada Currency INR'), ('other', 'Other')], verbose_name='Source'),
        ),
        migrations.AlterField(
            model_name='contribution',
            name='source',
            field=models.CharField(blank=True, max_length=30, default='', choices=[('tovp-f-mayapur', 'TOVP Fundraising Mayapur'), ('nityananda', 'Nityananda Tour'), ('jps-office', 'JPS Office'), ('namahatta', 'JPS Namahatta'), ('jps-others', 'JPS Others'), ('gkg-vp-2015', 'GKG Vyasa Puja 2015'), ('bcs-vp-2015', 'BCS Vyasa Puja 2015'), ('neel-vasan-das', 'Neel Vasan Das'), ('vvps-vp-2015', 'Vedavyasapriya Swami Vyasa Puja 2015'), ('rns-kartik-yatra', 'RNS Kartik Yatra'), ('j-w-marriot', 'J W Marriot'), ('kanjurmarg-mumbai-2015', 'Kanjurmarg Mumbai 2015'), ('nvs', 'Nava Yogendra Swami'), ('mso', 'MSO'), ('lm-reception', 'Life Membership Reception'), ('vrindavan-booth', 'Vrindavan Booth'), ('prabhupada-currency-inr', 'Prabhupada Currency INR'), ('other', 'Other')], verbose_name='Source'),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='source',
            field=models.CharField(blank=True, max_length=30, default='', choices=[('tovp-f-mayapur', 'TOVP Fundraising Mayapur'), ('nityananda', 'Nityananda Tour'), ('jps-office', 'JPS Office'), ('namahatta', 'JPS Namahatta'), ('jps-others', 'JPS Others'), ('gkg-vp-2015', 'GKG Vyasa Puja 2015'), ('bcs-vp-2015', 'BCS Vyasa Puja 2015'), ('neel-vasan-das', 'Neel Vasan Das'), ('vvps-vp-2015', 'Vedavyasapriya Swami Vyasa Puja 2015'), ('rns-kartik-yatra', 'RNS Kartik Yatra'), ('j-w-marriot', 'J W Marriot'), ('kanjurmarg-mumbai-2015', 'Kanjurmarg Mumbai 2015'), ('nvs', 'Nava Yogendra Swami'), ('mso', 'MSO'), ('lm-reception', 'Life Membership Reception'), ('vrindavan-booth', 'Vrindavan Booth'), ('prabhupada-currency-inr', 'Prabhupada Currency INR'), ('other', 'Other')], verbose_name='Source'),
        ),
    ]
