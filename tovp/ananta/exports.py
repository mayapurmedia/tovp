import csv
from operator import attrgetter

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

        # BOM (optional...Excel needs it to open UTF-8 file properly)
        response.write(u'\ufeff'.encode('utf8'))

        writer.writerow(self.generate_header())

        for result in self.results:
            self.obj = result.object
            writer.writerow(self.generate_row())
        return response
