from collections import OrderedDict

from ananta.exports import BaseExport


class ContactExport(BaseExport):
    def export_data(self):
        export_data = OrderedDict((
            ("Record ID", {'type': 'result', 'value': 'pk'}),
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
            ("Country", {'type': 'result', 'value': 'country'}),
            ("Yatra", {'type': 'result', 'value': 'yatra'}),

            ("Total Balance [USD]", {'type': 'result', 'value': 'balance_total_usd'}),
            ("Year Balance [USD]", {'type': 'result', 'value': 'balance_year_usd'}),
            ("Fin. Year Bal. [USD]", {'type': 'result', 'value': 'balance_financial_year_usd'}),

            ("Total Balance [INR]", {'type': 'result', 'value': 'balance_total_inr'}),
            ("Year Balance [INR]", {'type': 'result', 'value': 'balance_year_inr'}),
            ("Fin. Year Bal. [INR]", {'type': 'result', 'value': 'balance_financial_year_inr'}),

            ("Sources", {'type': 'result', 'value': 'sources'}),
            ("Promotions", {'type': 'result', 'value': 'promotions'}),
        ))
        return export_data
