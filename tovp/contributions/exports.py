import csv
from operator import attrgetter
from collections import OrderedDict

from django.utils.encoding import smart_str
from django.http import HttpResponse


class BaseExport(object):
    def __init__(self, results, *args, **kwargs):
        self.results = results
        super(BaseExport, self).__init__(*args, **kwargs)

    def get_value(self, value):
        return attrgetter(value)(self.obj)

    def generate_header(self):
        header = []
        for key in self.export_data().keys():
            header.append(smart_str(key))
        return header

    def generate_row(self):
        row = []
        for key in self.export_data():
            value = ''
            row_info = self.export_data()[key]
            if row_info['type'] == 'value':
                value = self.get_value(row_info['value'])
            if row_info['type'] == 'function':
                value = self.get_value(row_info['value'])()
            if row_info['type'] == 'custom':
                value = getattr(self, 'get_' + row_info['value'])()
            row.append(smart_str(value))
        return row

    def render(self):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=donate.tovp.org-export.csv'
        writer = csv.writer(response, csv.excel)
        response.write(u'\ufeff'.encode('utf8'))  # BOM (optional...Excel needs it to open UTF-8 file properly)

        writer.writerow(self.generate_header())

        for result in self.results:
            self.obj = result.object
            writer.writerow(self.generate_row())
        return response


class PledgeExport(BaseExport):
    def get_name(self):
        obj = self.obj
        name = ''
        if obj.person.name:
            name = obj.person.name
        else:
            name = obj.person.initiated_name
        return name

    def get_address(self):
        obj = self.obj
        address = ''
        if obj.person.address:
            address = obj.person.address
        return address

    def get_promotions(self):
        obj = self.obj
        promotions = []
        for promotion in obj.assigned_promotions():
            try:
                promotions.append(promotion._meta.verbose_name.title())
            except:
                promotions.appen('*Noname*')
        return ",".join(promotions)

    def export_data(self):
        export_data = OrderedDict((
            ("Record ID", {'type': 'value', 'value': 'pk'}),
            ("Legal Name", {'type': 'value', 'value': 'person.name'}),
            ("Initiated Name", {'type': 'value', 'value': 'person.initiated_name'}),
            ("Email", {'type': 'value', 'value': 'person.email'}),
            ("Phone Number", {'type': 'value', 'value': 'person.phone_number'}),
            ("Address", {'type': 'custom', 'value': 'address'}),
            ("City", {'type': 'value', 'value': 'person.city'}),
            ("ZIP code", {'type': 'value', 'value': 'person.postcode'}),
            ("State", {'type': 'value', 'value': 'person.state'}),
            ("Country", {'type': 'value', 'value': 'person.country.name'}),
            ("Amount", {'type': 'value', 'value': 'amount'}),
            ("Currency", {'type': 'value', 'value': 'currency'}),
            ("Source", {'type': 'function', 'value': 'get_source_display'}),
            ("Promotions", {'type': 'custom', 'value': 'promotions'}),
        ))
        return export_data


class ContributionExport(BaseExport):
    def get_receipt_date(self):
        obj = self.obj
        receipt_date = ''
        if obj.receipt_date:
            receipt_date = obj.receipt_date.strftime("%d %B %Y")
        elif obj.cleared_on:
            receipt_date = obj.cleared_on.strftime("%d %B %Y")
        return receipt_date

    def get_name(self):
        obj = self.obj
        name = ''
        if obj.overwrite_name:
            name = obj.overwrite_name
        elif obj.pledge.person.name:
            name = obj.pledge.person.name
        else:
            name = obj.pledge.person.initiated_name
        return name

    def get_address(self):
        obj = self.obj
        address = ''
        if obj.overwrite_address:
            address = obj.overwrite_address
        elif obj.pledge.person.address:
            address = obj.pledge.person.address
        return address

    def get_cleared_on(self):
        obj = self.obj
        cleared_on = ''
        if obj.cleared_on:
            cleared_on = obj.cleared_on.strftime("%d %B %Y")
        return cleared_on

    def get_dated(self):
        obj = self.obj
        dated = ''
        if obj.dated:
            dated = obj.dated.strftime("%d %B %Y")
        return dated

    def get_pan_card_number(self):
        obj = self.obj
        pan_card_number = ''
        if obj.overwrite_pan_card:
            pan_card_number = obj.overwrite_pan_card
        elif obj.pledge.person.pan_card_number:
            pan_card_number = obj.pledge.person.pan_card_number
        return pan_card_number

    def get_promotions(self):
        obj = self.obj
        promotions = []
        for promotion in obj.pledge.assigned_promotions():
            try:
                promotions.append(promotion._meta.verbose_name.title())
            except:
                promotions.appen('*Noname*')
        return ",".join(promotions)

    def get_collector(self):
        obj = self.obj
        collector = ''
        if obj.collector:
            collector = obj.collector.mixed_name
        return collector

    def export_data(self):
        export_data = OrderedDict((
            ("Record ID", {'type': 'value', 'value': 'pk'}),
            ("Mayapur Official Receipt", {'type': 'value', 'value': 'is_external'}),
            ("Receipt Date", {'type': 'custom', 'value': 'receipt_date'}),
            ("Name", {'type': 'custom', 'value': 'name'}),
            ("Email", {'type': 'value', 'value': 'pledge.person.email'}),
            ("Phone Number", {'type': 'value', 'value': 'pledge.person.phone_number'}),
            ("Address", {'type': 'custom', 'value': 'address'}),
            ("Serial Number", {'type': 'function', 'value': 'get_serial_number'}),
            ("Status", {'type': 'function', 'value': 'get_status_display'}),
            ("Amount", {'type': 'value', 'value': 'amount'}),
            ("Currency", {'type': 'value', 'value': 'currency'}),
            ("Payment Method", {'type': 'function', 'value': 'get_payment_method_display'}),
            ("Transaction ID", {'type': 'value', 'value': 'transaction_id'}),
            ("Cleared On", {'type': 'custom', 'value': 'cleared_on'}),
            ("Dated On", {'type': 'custom', 'value': 'dated'}),
            ("PAN Card No", {'type': 'custom', 'value': 'pan_card_number'}),
            ("Source", {'type': 'function', 'value': 'get_source_display'}),
            ("Promotions", {'type': 'custom', 'value': 'promotions'}),
            ("Collector", {'type': 'custom', 'value': 'collector'}),
        ))
        return export_data