from collections import OrderedDict

from ananta.exports import BaseExport


class ContactExport(BaseExport):
    def get_name(self):
        obj = self.obj
        name = ''
        if obj.name:
            name = obj.name
        else:
            name = obj.initiated_name
        return name

    def get_address(self):
        obj = self.obj
        address = ''
        if obj.address:
            address = obj.address
        return address

    def get_sources(self):
        obj = self.obj

        items = []
        for pledge in obj.pledges.all():
            if (pledge.get_source_display()) and (pledge.get_source_display() not in items):
                items.append(pledge.get_source_display())
            for contribution in pledge.contributions.all():
                if (contribution.get_source_display()) and (contribution.get_source_display() not in items):
                    items.append(pledge.get_source_display())
        return ",".join(items)

    def get_promotions(self):
        obj = self.obj
        promotions = []
        for promotion in obj.assigned_promotions():
            try:
                promotions.append(promotion._meta.verbose_name.title())
            except:
                promotions.appen('*Noname*')
        return ",".join(promotions)

    def get_balance_total_usd(self):
        obj = self.obj
        balance = obj.get_ballance()
        return balance['USD']['paid']

    def get_balance_total_inr(self):
        obj = self.obj
        balance = obj.get_ballance()
        return balance['INR']['paid']

    def get_balance_year_usd(self):
        obj = self.obj
        balance = obj.get_ballance()
        return balance['USD']['donated_year']

    def get_balance_year_inr(self):
        obj = self.obj
        balance = obj.get_ballance()
        return balance['INR']['donated_year']

    def get_balance_financial_year_usd(self):
        obj = self.obj
        balance = obj.get_ballance()
        return balance['USD']['donated_financial_year']

    def get_balance_financial_year_inr(self):
        obj = self.obj
        balance = obj.get_ballance()
        return balance['INR']['donated_financial_year']

    def export_data(self):
        export_data = OrderedDict((
            ("Record ID", {'type': 'value', 'value': 'pk'}),
            ("First Name", {'type': 'value', 'value': 'first_name'}),
            ("Middle Name", {'type': 'value', 'value': 'middle_name'}),
            ("Last Name", {'type': 'value', 'value': 'last_name'}),
            ("Initiated Name", {'type': 'value', 'value': 'initiated_name'}),

            ("Email", {'type': 'value', 'value': 'email'}),
            ("Phone Number", {'type': 'value', 'value': 'phone_number'}),
            ("Address", {'type': 'custom', 'value': 'address'}),
            ("City", {'type': 'value', 'value': 'city'}),
            ("ZIP code", {'type': 'value', 'value': 'postcode'}),
            ("State", {'type': 'value', 'value': 'state'}),
            ("Country", {'type': 'value', 'value': 'country.name'}),
            ("Yatra", {'type': 'function', 'value': 'get_yatra_display'}),

            ("Total Balance [USD]", {'type': 'custom', 'value': 'balance_total_usd'}),
            ("Year Balance [USD]", {'type': 'custom', 'value': 'balance_year_usd'}),
            ("Fin. Year Bal. [USD]", {'type': 'custom', 'value': 'balance_financial_year_usd'}),

            ("Total Balance [INR]", {'type': 'custom', 'value': 'balance_total_inr'}),
            ("Year Balance [INR]", {'type': 'custom', 'value': 'balance_year_inr'}),
            ("Fin. Year Bal. [INR]", {'type': 'custom', 'value': 'balance_financial_year_inr'}),

            ("Sources", {'type': 'custom', 'value': 'sources'}),
            ("Promotions", {'type': 'custom', 'value': 'promotions'}),
        ))
        return export_data
