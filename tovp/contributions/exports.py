from collections import OrderedDict

from ananta.exports import BaseExport


class PledgeExport(BaseExport):
    def get_source(self):
        source = self.result.source
        return ','.join(source)

    def get_promotion_type(self):
        promotions = self.result.promotion_type
        return ",".join(promotions)

    def export_data(self):
        export_data = OrderedDict((
            ("Record ID", {'type': 'result', 'value': 'pk'}),
            ("Contact Record ID", {'type': 'value', 'value': 'person.pk'}),

            ("First Name", {'type': 'result', 'value': 'first_name'}),
            ("Middle Name", {'type': 'result', 'value': 'middle_name'}),
            ("Last Name", {'type': 'result', 'value': 'last_name'}),
            ("Initiated Name", {'type': 'result', 'value': 'initiated_name'}),
            ("Email", {'type': 'result', 'value': 'email'}),
            ("Phone Number", {'type': 'result', 'value': 'phone_number'}),
            ("Address", {'type': 'result', 'value': 'address'}),

            ("City", {'type': 'result', 'value': 'city'}),
            ("ZIP code", {'type': 'result', 'value': 'postcode'}),
            ("State", {'type': 'result', 'value': 'state'}),
            ("Country", {'type': 'result', 'value': 'name'}),
            ("Amount", {'type': 'result', 'value': 'amount'}),
            ("Amount Paid", {'type': 'result', 'value': 'amount_paid'}),
            ("Currency", {'type': 'result', 'value': 'currency'}),

            ("Percent Paid", {'type': 'result', 'value': 'progress'}),

            ("Source", {'type': 'custom', 'value': 'source'}),
            ("Promotions", {'type': 'custom', 'value': 'promotion_type'}),
        ))
        return export_data


class ContributionExport(BaseExport):
    def get_promotion_type(self):
        promotions = self.result.promotion_type
        return ",".join(promotions)

    def get_source(self):
        source = self.result.source
        return ','.join(source)

    def export_data(self):
        export_data = OrderedDict((
            ("Record ID", {'type': 'result', 'value': 'pk'}),
            ("Mayapur Official Receipt", {'type': 'result', 'value': 'is_external'}),
            ("Receipt Date", {'type': 'result', 'value': 'receipt_date'}),
            ("First Name", {'type': 'result', 'value': 'first_name'}),
            ("Middle Name", {'type': 'result', 'value': 'middle_name'}),
            ("Last Name", {'type': 'result', 'value': 'last_name'}),
            ("Initiated Name", {'type': 'result', 'value': 'initiated_name'}),
            ("Email", {'type': 'result', 'value': 'email'}),
            ("Phone Number", {'type': 'result', 'value': 'phone_number'}),
            ("Address", {'type': 'result', 'value': 'address'}),

            ("Serial Number", {'type': 'result', 'value': 'serial_number'}),
            ("Status", {'type': 'result', 'value': 'status'}),
            ("Amount", {'type': 'result', 'value': 'amount'}),
            ("Currency", {'type': 'result', 'value': 'currency'}),
            ("Payment Method", {'type': 'result', 'value': 'payment_method'}),
            ("Transaction/Cheque ID", {'type': 'result', 'value': 'transaction_id'}),
            ("Cleared On", {'type': 'result', 'value': 'cleared_on'}),
            ("Dated On", {'type': 'result', 'value': 'dated'}),
            ("PAN Card No", {'type': 'result', 'value': 'pan_card_number'}),

            ("Source", {'type': 'custom', 'value': 'source'}),
            ("Promotions", {'type': 'custom', 'value': 'promotion_type'}),

            ("Note", {'type': 'result', 'value': 'note'}),
        ))
        return export_data
