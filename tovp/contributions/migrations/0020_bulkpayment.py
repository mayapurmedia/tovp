# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import ananta.models
from django.conf import settings
import audit_log.models.fields
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0008_auto_20150405_1214'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contributions', '0019_remove_contribution_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='BulkPayment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('source', models.CharField(verbose_name='Source', choices=[('nityananda', 'Nityananda Tour'), ('jps-office', 'JPS Office'), ('namahatta', 'JPS Namahatta'), ('jps-others', 'JPS Others'), ('nvs', 'Nava Yogendra Swami'), ('mso', 'MSO'), ('lm-reception', 'Life Membership Reception'), ('vrindavan-booth', 'Vrindavan Booth'), ('prabhupada-currency-inr', 'Prabhupada Currency INR'), ('other', 'Other')], blank=True, default='', max_length=30)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False)),
                ('serial_year', models.CharField(verbose_name='Serial Number Year', help_text='Serial Number Year of this contribution.', blank=True, max_length=5)),
                ('serial_number', models.CharField(verbose_name='Serial Number', help_text='Serial Number of this contribution for financial year.', blank=True, max_length=5)),
                ('amount', models.DecimalField(decimal_places=2, verbose_name='Amount', max_digits=20)),
                ('currency', models.CharField(verbose_name='Currency', choices=[('INR', '₹ (INR)'), ('USD', '$ (USD)'), ('EUR', '€ (EUR)'), ('GBP', '£ (GBP)')], default='INR', max_length=6)),
                ('payment_method', models.CharField(verbose_name='Payment Method', choices=[('cashl', 'Cash (Indian)'), ('cashf', 'Cash (Foreign)'), ('ccdcsl', 'Credit/Debit Card Swipe Local'), ('ccdcsf', 'Credit/Debit Card Swipe Foreign'), ('neftl', 'NEFT (Indian)'), ('neftf', 'NEFT (Foreign)'), ('chequel', 'Cheque (Indian)'), ('chequef', 'Cheque (Foreign)'), ('paypal', 'Paypal'), ('axis', 'Gateway Axis (Internet)')], max_length=16)),
                ('transaction_id', models.CharField(verbose_name='Transaction ID or Cheque No', help_text='Transaction ID of this contribution or cheque number.', blank=True, max_length=100)),
                ('bank', models.CharField(verbose_name='Bank', help_text='Write bank name (and possible branch or location) for cheque', blank=True, max_length=100)),
                ('dated', models.DateField(verbose_name='Dated', null=True, blank=True, help_text='Enter date on the cheque')),
                ('receipt_date', models.DateField(verbose_name='Receipt Date', null=True, blank=True, help_text='Enter date which should be on the receipt.')),
                ('cleared_on', models.DateField(verbose_name='Cleared On', null=True, blank=True, help_text='Enter date when transaction was completed (money came to TOVP)')),
                ('status', models.CharField(verbose_name='Status', choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], max_length=30)),
                ('status_changed', model_utils.fields.MonitorField(monitor='status', default=django.utils.timezone.now)),
                ('book_number', models.CharField(verbose_name='Book Number', help_text='Enter if you are entering contribution from book', blank=True, max_length=20)),
                ('slip_number', models.CharField(verbose_name='Slip Number', help_text='Enter if you are entering contribution from slip', blank=True, max_length=20)),
                ('overwrite_name', models.CharField(verbose_name='Name who pays on behalf of main contact', blank=True, max_length=255)),
                ('overwrite_address', models.CharField(verbose_name='Address who pays on behalf of main contact', blank=True, max_length=255)),
                ('receipt_type', models.CharField(verbose_name='Receipt Type', choices=[('official', 'Official'), ('acknowledgement', 'Not official / Acknowledgement')], max_length=100)),
                ('created_by', audit_log.models.fields.CreatingUserField(verbose_name='created by', related_name='created_contributions_bulkpayment_set', to=settings.AUTH_USER_MODEL, null=True, editable=False)),
                ('modified_by', audit_log.models.fields.LastUserField(verbose_name='modified by', related_name='modified_contributions_bulkpayment_set', to=settings.AUTH_USER_MODEL, null=True, editable=False)),
                ('person', models.ForeignKey(verbose_name='Person', blank=True, related_name='bulk_payments', to='contacts.Person')),
            ],
            options={
                'abstract': False,
            },
            bases=(ananta.models.NextPrevMixin, models.Model),
        ),
    ]
