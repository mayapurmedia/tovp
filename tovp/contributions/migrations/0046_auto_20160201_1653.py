# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0045_auto_20160112_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulkpayment',
            name='source',
            field=models.CharField(choices=[('tovp-f-mayapur', 'TOVP Fundraising Mayapur'), ('nityananda', 'Nityananda Tour'), ('jps-office', 'JPS Office'), ('namahatta', 'JPS Namahatta'), ('jps-others', 'JPS Others'), ('gkg-vp-2015', 'GKG Vyasa Puja 2015'), ('bcs-vp-2015', 'BCS Vyasa Puja 2015'), ('neel-vasan-das', 'Neel Vasan Das'), ('vvps-vp-2015', 'Vedavyasapriya Swami Vyasa Puja 2015'), ('rns-kartik-yatra', 'RNS Kartik Yatra'), ('j-w-marriot', 'J W Marriot'), ('kanjurmarg-mumbai-2015', 'Kanjurmarg Mumbai 2015'), ('nvs', 'Nava Yogendra Swami'), ('mso', 'MSO'), ('lm-reception', 'Life Membership Reception'), ('vrindavan-booth', 'Vrindavan Booth'), ('prabhupada-currency-inr', 'Prabhupada Currency INR'), ('mayapur-community', 'Mayapur Community'), ('delhi-vidyanagar-2015', 'Delhi Vidyanagar 2015'), ('pune-group-mayapur-2015', 'Pune Group Mayapur 2015'), ('bhagavata-saptaha-2015', 'Bhagavata Saptaha 2015'), ('rohini-narayani', 'Rohini (Sri Narayani Devi Dasi)'), ('bhakti-vriksa-kolkata-2016', 'Bhakti Vriksa Kolkata 2016'), ('other', 'Other')], default='', verbose_name='Source', blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='contribution',
            name='source',
            field=models.CharField(choices=[('tovp-f-mayapur', 'TOVP Fundraising Mayapur'), ('nityananda', 'Nityananda Tour'), ('jps-office', 'JPS Office'), ('namahatta', 'JPS Namahatta'), ('jps-others', 'JPS Others'), ('gkg-vp-2015', 'GKG Vyasa Puja 2015'), ('bcs-vp-2015', 'BCS Vyasa Puja 2015'), ('neel-vasan-das', 'Neel Vasan Das'), ('vvps-vp-2015', 'Vedavyasapriya Swami Vyasa Puja 2015'), ('rns-kartik-yatra', 'RNS Kartik Yatra'), ('j-w-marriot', 'J W Marriot'), ('kanjurmarg-mumbai-2015', 'Kanjurmarg Mumbai 2015'), ('nvs', 'Nava Yogendra Swami'), ('mso', 'MSO'), ('lm-reception', 'Life Membership Reception'), ('vrindavan-booth', 'Vrindavan Booth'), ('prabhupada-currency-inr', 'Prabhupada Currency INR'), ('mayapur-community', 'Mayapur Community'), ('delhi-vidyanagar-2015', 'Delhi Vidyanagar 2015'), ('pune-group-mayapur-2015', 'Pune Group Mayapur 2015'), ('bhagavata-saptaha-2015', 'Bhagavata Saptaha 2015'), ('rohini-narayani', 'Rohini (Sri Narayani Devi Dasi)'), ('bhakti-vriksa-kolkata-2016', 'Bhakti Vriksa Kolkata 2016'), ('other', 'Other')], default='', verbose_name='Source', blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='source',
            field=models.CharField(choices=[('tovp-f-mayapur', 'TOVP Fundraising Mayapur'), ('nityananda', 'Nityananda Tour'), ('jps-office', 'JPS Office'), ('namahatta', 'JPS Namahatta'), ('jps-others', 'JPS Others'), ('gkg-vp-2015', 'GKG Vyasa Puja 2015'), ('bcs-vp-2015', 'BCS Vyasa Puja 2015'), ('neel-vasan-das', 'Neel Vasan Das'), ('vvps-vp-2015', 'Vedavyasapriya Swami Vyasa Puja 2015'), ('rns-kartik-yatra', 'RNS Kartik Yatra'), ('j-w-marriot', 'J W Marriot'), ('kanjurmarg-mumbai-2015', 'Kanjurmarg Mumbai 2015'), ('nvs', 'Nava Yogendra Swami'), ('mso', 'MSO'), ('lm-reception', 'Life Membership Reception'), ('vrindavan-booth', 'Vrindavan Booth'), ('prabhupada-currency-inr', 'Prabhupada Currency INR'), ('mayapur-community', 'Mayapur Community'), ('delhi-vidyanagar-2015', 'Delhi Vidyanagar 2015'), ('pune-group-mayapur-2015', 'Pune Group Mayapur 2015'), ('bhagavata-saptaha-2015', 'Bhagavata Saptaha 2015'), ('rohini-narayani', 'Rohini (Sri Narayani Devi Dasi)'), ('bhakti-vriksa-kolkata-2016', 'Bhakti Vriksa Kolkata 2016'), ('other', 'Other')], default='', verbose_name='Source', blank=True, max_length=30),
        ),
    ]
