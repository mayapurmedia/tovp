from collections import OrderedDict

from ananta.exports import BaseExport


class PromotionExport(BaseExport):
    def get_promotion_name(self):
        return str(self.result.object._meta.verbose_name.title())

    def get_name(self):
        obj = self.result.object
        name = ''
        if obj.pledge.person.name:
            name = obj.pledge.person.name
        else:
            name = obj.pledge.person.initiated_name
        return name

    def get_address(self):
        obj = self.result.object
        address = ''
        if obj.pledge.person.address:
            address = obj.pledge.person.address
        return address

    def get_progress(self):
        obj = self.result.object
        return "{progress:.2f}%".format(progress=obj.pledge.progress)

    def get_name_on_brick(self):
        return self.result.name_on_brick

    def export_data(self):
        export_data = OrderedDict((
            ("Record ID", {'type': 'value', 'value': 'pk'}),
            ("Promotion", {'type': 'custom', 'value': 'promotion_name'}),
            ("Name", {'type': 'custom', 'value': 'name'}),
            ("First Name", {'type': 'value', 'value': 'pledge.person.first_name'}),
            ("Middle Name", {'type': 'value', 'value': 'pledge.person.middle_name'}),
            ("Last Name", {'type': 'value', 'value': 'pledge.person.last_name'}),
            ("Initiated Name", {'type': 'value', 'value': 'pledge.person.initiated_name'}),
            ("Email", {'type': 'value', 'value': 'pledge.person.email'}),
            ("Phone Number", {'type': 'value', 'value': 'pledge.person.phone_number'}),
            ("Address", {'type': 'custom', 'value': 'address'}),
            ("Percent Paid", {'type': 'custom', 'value': 'progress'}),
            ("Brick Name", {'type': 'custom', 'value': 'name_on_brick'}),
        ))
        return export_data
