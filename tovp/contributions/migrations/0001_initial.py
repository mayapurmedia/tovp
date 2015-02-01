# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('amount', models.DecimalField(decimal_places=2, verbose_name='Amount', max_digits=20)),
                ('currency', models.CharField(default='INR', choices=[('INR', '₹'), ('USD', '$'), ('EUR', '€')], max_length=6, verbose_name='Currency')),
                ('payment_method', models.CharField(choices=[('cashl', 'Cash (Indian)'), ('cashf', 'Cash (Foreign)'), ('ccdcsl', 'Credit/Debit Card Swipe Local'), ('ccdcsf', 'Credit/Debit Card Swipe Foreign'), ('neftl', 'NEFT (Indian)'), ('neftf', 'NEFT (Foreign)'), ('chequl', 'Cheque (Indian)'), ('chequf', 'Cheque (Foreign)')], max_length=6, verbose_name='Payment Method')),
                ('transaction_id', models.CharField(help_text='Transaction ID of this contribution or cheque number.', max_length=100, verbose_name='Transaction ID or Cheque No', blank=True)),
                ('dated', models.DateField(help_text='Enter date of the transaction (e.g. date on the cheque, date when credit card was charged)', null=True, verbose_name='Dated', blank=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], max_length=30, verbose_name='Status')),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status')),
                ('person', models.ForeignKey(to='contacts.Person', verbose_name='Person', blank=True, related_name='contributions')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pledge',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('amount', models.DecimalField(decimal_places=2, verbose_name='Amount', max_digits=20)),
                ('amount_paid', models.DecimalField(decimal_places=2, verbose_name='Amount Paid', max_digits=20, blank=True, default=0, null=True)),
                ('currency', models.CharField(default='INR', choices=[('INR', '₹'), ('USD', '$'), ('EUR', '€')], max_length=6, verbose_name='Currency')),
                ('payments_start_date', models.DateField(help_text='Date of first expected payment for this pledge.', null=True, verbose_name='Payments Start', blank=True)),
                ('interval', models.CharField(help_text='Enter planned interval of payments (e.g. 1 month)', choices=[('1', '1 month'), ('2', '2 months'), ('3', '3 months'), ('4', '4 months'), ('6', '6 months')], max_length=30, verbose_name='Payments Interval')),
                ('status', models.CharField(default='pending', choices=[('pending', 'Pending'), ('partial', 'Partially Paid'), ('completed', 'Completed'), ('failed', 'Shadow')], max_length=30, verbose_name='Status', blank=True)),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status')),
                ('next_payment_date', models.DateField(help_text='Date of next expected payment.', null=True, verbose_name='Next Payment Date', blank=True)),
                ('person', models.ForeignKey(to='contacts.Person', verbose_name='Person', blank=True, related_name='pledges')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contribution',
            name='pledge',
            field=models.ForeignKey(to='contributions.Pledge', verbose_name='Pledge', blank=True, related_name='contributions', null=True),
            preserve_default=True,
        ),
    ]
