# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0046_auto_20160201_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulkpayment',
            name='source',
            field=models.CharField(default='', choices=[('tovp-f-mayapur', 'TOVP Fundraising Mayapur'), ('bcs-vp-2015', 'BCS Vyasa Puja 2015'), ('bhagavata-saptaha-2015', 'Bhagavata Saptaha 2015'), ('bhakti-vriksa-kolkata-2016', 'Bhakti Vriksa Kolkata 2016'), ('braj-mohan-mumbai', 'Braj Mohan (Mumbai)'), ('delhi-vidyanagar-2015', 'Delhi Vidyanagar 2015'), ('gkg-vp-2015', 'GKG Vyasa Puja 2015'), ('ils-2016', 'ILS 2016'), ('j-w-marriot', 'J W Marriot'), ('jps-office', 'JPS Office'), ('jps-others', 'JPS Others'), ('kanjurmarg-mumbai-2015', 'Kanjurmarg Mumbai 2015'), ('lm-reception', 'Life Membership Reception'), ('mayapur-community', 'Mayapur Community'), ('mso', 'MSO'), ('mumbai-yatra-2016', 'Mumbai Yatra 2016'), ('namahatta', 'JPS Namahatta'), ('neel-vasan-das', 'Neel Vasan Das'), ('nigdi-2016.', 'Nigdi 2016.'), ('nityananda', 'Nityananda Tour'), ('nvs', 'Nava Yogendra Swami'), ('other', 'Other'), ('prabhupada-currency-inr', 'Prabhupada Currency INR'), ('pune-group-mayapur-2015', 'Pune Group Mayapur 2015'), ('pune-yatra-2016', 'Pune Yatra 2016'), ('rns-kartik-yatra', 'RNS Kartik Yatra'), ('rohini-narayani', 'Rohini (Sri Narayani Devi Dasi)'), ('vrindavan-booth', 'Vrindavan Booth'), ('vvps-vp-2015', 'Vedavyasapriya Swami Vyasa Puja 2015')], blank=True, verbose_name='Source', max_length=30),
        ),
        migrations.AlterField(
            model_name='contribution',
            name='source',
            field=models.CharField(default='', choices=[('tovp-f-mayapur', 'TOVP Fundraising Mayapur'), ('bcs-vp-2015', 'BCS Vyasa Puja 2015'), ('bhagavata-saptaha-2015', 'Bhagavata Saptaha 2015'), ('bhakti-vriksa-kolkata-2016', 'Bhakti Vriksa Kolkata 2016'), ('braj-mohan-mumbai', 'Braj Mohan (Mumbai)'), ('delhi-vidyanagar-2015', 'Delhi Vidyanagar 2015'), ('gkg-vp-2015', 'GKG Vyasa Puja 2015'), ('ils-2016', 'ILS 2016'), ('j-w-marriot', 'J W Marriot'), ('jps-office', 'JPS Office'), ('jps-others', 'JPS Others'), ('kanjurmarg-mumbai-2015', 'Kanjurmarg Mumbai 2015'), ('lm-reception', 'Life Membership Reception'), ('mayapur-community', 'Mayapur Community'), ('mso', 'MSO'), ('mumbai-yatra-2016', 'Mumbai Yatra 2016'), ('namahatta', 'JPS Namahatta'), ('neel-vasan-das', 'Neel Vasan Das'), ('nigdi-2016.', 'Nigdi 2016.'), ('nityananda', 'Nityananda Tour'), ('nvs', 'Nava Yogendra Swami'), ('other', 'Other'), ('prabhupada-currency-inr', 'Prabhupada Currency INR'), ('pune-group-mayapur-2015', 'Pune Group Mayapur 2015'), ('pune-yatra-2016', 'Pune Yatra 2016'), ('rns-kartik-yatra', 'RNS Kartik Yatra'), ('rohini-narayani', 'Rohini (Sri Narayani Devi Dasi)'), ('vrindavan-booth', 'Vrindavan Booth'), ('vvps-vp-2015', 'Vedavyasapriya Swami Vyasa Puja 2015')], blank=True, verbose_name='Source', max_length=30),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='source',
            field=models.CharField(default='', choices=[('tovp-f-mayapur', 'TOVP Fundraising Mayapur'), ('bcs-vp-2015', 'BCS Vyasa Puja 2015'), ('bhagavata-saptaha-2015', 'Bhagavata Saptaha 2015'), ('bhakti-vriksa-kolkata-2016', 'Bhakti Vriksa Kolkata 2016'), ('braj-mohan-mumbai', 'Braj Mohan (Mumbai)'), ('delhi-vidyanagar-2015', 'Delhi Vidyanagar 2015'), ('gkg-vp-2015', 'GKG Vyasa Puja 2015'), ('ils-2016', 'ILS 2016'), ('j-w-marriot', 'J W Marriot'), ('jps-office', 'JPS Office'), ('jps-others', 'JPS Others'), ('kanjurmarg-mumbai-2015', 'Kanjurmarg Mumbai 2015'), ('lm-reception', 'Life Membership Reception'), ('mayapur-community', 'Mayapur Community'), ('mso', 'MSO'), ('mumbai-yatra-2016', 'Mumbai Yatra 2016'), ('namahatta', 'JPS Namahatta'), ('neel-vasan-das', 'Neel Vasan Das'), ('nigdi-2016.', 'Nigdi 2016.'), ('nityananda', 'Nityananda Tour'), ('nvs', 'Nava Yogendra Swami'), ('other', 'Other'), ('prabhupada-currency-inr', 'Prabhupada Currency INR'), ('pune-group-mayapur-2015', 'Pune Group Mayapur 2015'), ('pune-yatra-2016', 'Pune Yatra 2016'), ('rns-kartik-yatra', 'RNS Kartik Yatra'), ('rohini-narayani', 'Rohini (Sri Narayani Devi Dasi)'), ('vrindavan-booth', 'Vrindavan Booth'), ('vvps-vp-2015', 'Vedavyasapriya Swami Vyasa Puja 2015')], blank=True, verbose_name='Source', max_length=30),
        ),
    ]
