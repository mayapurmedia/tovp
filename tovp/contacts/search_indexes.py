from haystack import indexes

from ananta.search_indexes import ContentSearchIndexMixin

from .models import Person

COUNTRIES_TO_ZONES = {
    'AF': 'Asia',
    'AX': 'Others',
    'AL': 'Others',
    'DZ': 'Others',
    'AS': 'Others',
    'AD': 'Others',
    'AO': 'Others',
    'AI': 'Others',
    'AQ': 'Others',
    'AG': 'Others',
    'AR': 'Others',
    'AM': 'Others',
    'AW': 'Others',
    'AU': 'Australia',
    'AT': 'Europe',
    'AZ': 'Others',
    'BS': 'Others',
    'BH': 'Middle East',
    'BD': 'Others',
    'BB': 'Others',
    'BY': 'Europe',
    'BE': 'Europe',
    'BZ': 'Others',
    'BJ': 'Others',
    'BM': 'Others',
    'BT': 'Others',
    'BO': 'Others',
    'BQ': 'Others',
    'BA': 'Europe',
    'BW': 'Others',
    'BV': 'Others',
    'BR': 'Others',
    'IO': 'Others',
    'BN': 'Others',
    'BG': 'Europe',
    'BF': 'Others',
    'BI': 'Others',
    'CV': 'Others',
    'KH': 'Others',
    'CM': 'Others',
    'CA': 'Canada',
    'KY': 'Others',
    'CF': 'Others',
    'TD': 'Others',
    'CL': 'Others',
    'CN': 'Others',
    'CX': 'Others',
    'CC': 'Others',
    'CO': 'Others',
    'KM': 'Others',
    'CD': 'Others',
    'CG': 'Others',
    'CK': 'Others',
    'CR': 'Others',
    'CI': 'Others',
    'HR': 'Europe',
    'CU': 'Others',
    'CW': 'Others',
    'CY': 'Europe',
    'CZ': 'Europe',
    'DK': 'Europe',
    'DJ': 'Others',
    'DM': 'Others',
    'DO': 'Others',
    'EC': 'Others',
    'EG': 'Others',
    'SV': 'Others',
    'GQ': 'Others',
    'ER': 'Others',
    'EE': 'Europe',
    'ET': 'Others',
    'FK': 'Others',
    'FO': 'Others',
    'FJ': 'Asia',
    'FI': 'Europe',
    'FR': 'Europe',
    'GF': 'Others',
    'PF': 'Others',
    'TF': 'Others',
    'GA': 'Others',
    'GM': 'Others',
    'GE': 'Others',
    'DE': 'Europe',
    'GH': 'Others',
    'GI': 'Others',
    'GR': 'Europe',
    'GL': 'Others',
    'GD': 'Others',
    'GP': 'Others',
    'GU': 'Others',
    'GT': 'Others',
    'GG': 'Others',
    'GN': 'Others',
    'GW': 'Others',
    'GY': 'Others',
    'HT': 'Others',
    'HM': 'Others',
    'VA': 'Others',
    'HN': 'Others',
    'HK': 'Others',
    'HU': 'Europe',
    'IS': 'Europe',
    'IN': 'India',
    'ID': 'Asia',
    'IR': 'Others',
    'IQ': 'Others',
    'IE': 'Europe',
    'IM': 'Others',
    'IL': 'Others',
    'IT': 'Europe',
    'JM': 'Others',
    'JP': 'Others',
    'JE': 'Others',
    'JO': 'Others',
    'KZ': 'Russia',
    'KE': 'Others',
    'KI': 'Others',
    'KP': 'Asia',
    'KR': 'Asia',
    'KW': 'Middle East',
    'KG': 'Others',
    'LA': 'Others',
    'LV': 'Europe',
    'LB': 'Others',
    'LS': 'Others',
    'LR': 'Others',
    'LY': 'Others',
    'LI': 'Europe',
    'LT': 'Europe',
    'LU': 'Europe',
    'MO': 'Others',
    'MK': 'Europe',
    'MG': 'Others',
    'MW': 'Others',
    'MY': 'Asia',
    'MV': 'Others',
    'ML': 'Others',
    'MT': 'Europe',
    'MH': 'Others',
    'MQ': 'Others',
    'MR': 'Others',
    'MU': 'Others',
    'YT': 'Others',
    'MX': 'Others',
    'FM': 'Others',
    'MD': 'Europe',
    'MC': 'Europe',
    'MN': 'Others',
    'ME': 'Europe',
    'MS': 'Others',
    'MA': 'Others',
    'MZ': 'Others',
    'MM': 'Others',
    'NA': 'Others',
    'NR': 'Others',
    'NP': 'Others',
    'NL': 'Europe',
    'NC': 'Others',
    'NZ': 'Others',
    'NI': 'Others',
    'NE': 'Others',
    'NG': 'Others',
    'NU': 'Others',
    'NF': 'Others',
    'MP': 'Others',
    'NO': 'Europe',
    'OM': 'Others',
    'PK': 'Others',
    'PW': 'Others',
    'PS': 'Others',
    'PA': 'Others',
    'PG': 'Others',
    'PY': 'Others',
    'PE': 'Others',
    'PH': 'Others',
    'PN': 'Others',
    'PL': 'Europe',
    'PT': 'Europe',
    'PR': 'Others',
    'QA': 'Middle East',
    'RE': 'Others',
    'RO': 'Europe',
    'RU': 'Russia',
    'RW': 'Others',
    'BL': 'Others',
    'SH': 'Others',
    'KN': 'Others',
    'LC': 'Others',
    'MF': 'Others',
    'PM': 'Others',
    'VC': 'Others',
    'WS': 'Others',
    'SM': 'Europe',
    'ST': 'Others',
    'SA': 'Others',
    'SN': 'Others',
    'RS': 'Europe',
    'SC': 'Others',
    'SL': 'Others',
    'SG': 'Asia',
    'SX': 'Others',
    'SK': 'Europe',
    'SI': 'Europe',
    'SB': 'Others',
    'SO': 'Others',
    'ZA': 'South Africa',
    'GS': 'Others',
    'SS': 'Others',
    'ES': 'Europe',
    'LK': 'Others',
    'SD': 'Others',
    'SR': 'Others',
    'SJ': 'Others',
    'SZ': 'Others',
    'SE': 'Europe',
    'CH': 'Europe',
    'SY': 'Others',
    'TW': 'Others',
    'TJ': 'Others',
    'TZ': 'Others',
    'TH': 'Asia',
    'TL': 'Others',
    'TG': 'Others',
    'TK': 'Others',
    'TO': 'Others',
    'TT': 'Others',
    'TN': 'Others',
    'TR': 'Others',
    'TM': 'Others',
    'TC': 'Others',
    'TV': 'Others',
    'UG': 'Others',
    'UA': 'Russia',
    'AE': 'Others',
    'GB': 'UK',
    'UM': 'Others',
    'US': 'USA',
    'UY': 'Others',
    'UZ': 'Others',
    'VU': 'Others',
    'VE': 'Others',
    'VN': 'Others',
    'VG': 'Others',
    'VI': 'Others',
    'WF': 'Others',
    'EH': 'Others',
    'YE': 'Middle East',
    'ZM': 'Others',
    'ZW': 'Others',
}

class PersonIndex(ContentSearchIndexMixin, indexes.SearchIndex,
                  indexes.Indexable):
    content_name = 'Contact'
    text = indexes.CharField(document=True, use_template=True)
    mixed_name = indexes.CharField()
    full_name = indexes.CharField(model_attr='full_name')
    initiated_name = indexes.CharField(model_attr='initiated_name')
    first_name = indexes.CharField(model_attr='first_name')
    middle_name = indexes.CharField(model_attr='last_name')
    last_name = indexes.CharField(model_attr='last_name')
    email = indexes.CharField(model_attr='email')
    phone_number = indexes.CharField(model_attr='phone_number')
    yatra = indexes.CharField(faceted=True)
    address = indexes.CharField(model_attr='address')
    city = indexes.CharField(model_attr='city')
    state = indexes.CharField(model_attr='state')
    old_database_id = indexes.CharField(model_attr='old_database_id', null=True)
    country = indexes.CharField(model_attr='get_country_display', faceted=True)
    zone = indexes.CharField(faceted=True)
    postcode = indexes.CharField(model_attr='postcode')
    pan_card_number = indexes.CharField(model_attr='pan_card_number', null=True)
    note = indexes.CharField(model_attr='note')
    gifts = indexes.MultiValueField(null=True, faceted=True)
    promotion_type = indexes.MultiValueField(null=True, faceted=True)

    balance_total_usd = indexes.IntegerField()
    balance_year_usd = indexes.IntegerField()
    balance_financial_year_usd = indexes.IntegerField()

    balance_total_usd = indexes.IntegerField()
    balance_year_usd = indexes.IntegerField()
    balance_financial_year_usd = indexes.IntegerField()

    balance_total_inr = indexes.IntegerField()
    balance_year_inr = indexes.IntegerField()
    balance_financial_year_inr = indexes.IntegerField()

    sources = indexes.CharField(null=True)
    promotions = indexes.CharField(null=True)

    def prepare_gifts(self, obj):
        items = []
        if obj.gifts.count():
            for gift_given in obj.gifts.all():
                items.append(gift_given.gift.name)
        return items

    def prepare_promotion_type(self, obj):
        items = []
        for promotion in obj.assigned_promotions():
            try:
                items.append(promotion._meta.verbose_name.title())
            except:
                items.append('Noname')
        return items

    def prepare_mixed_name(self, obj):
        return obj.join_fields(
            ('initiated_name', 'first_name', 'middle_name', 'last_name'),
            separator=" ").replace('.', '. ').replace('-', ' ')

    def prepare_yatra(self, obj):
        if obj.yatra:
            return obj.get_yatra_display()
        else:
            return 'None'

    def prepare_zone(self, obj):
        if obj.country in COUNTRIES_TO_ZONES:
            return COUNTRIES_TO_ZONES[obj.country]
        else:
            return 'No Zone'

    def prepare_sources(self, obj):
        items = []
        for pledge in obj.pledges.all():
            if (pledge.get_source_display()) and (pledge.get_source_display() not in items):
                items.append(pledge.get_source_display())
            for contribution in pledge.contributions.all():
                if (contribution.get_source_display()) and (contribution.get_source_display() not in items):
                    items.append(pledge.get_source_display())
        return ",".join(items)

    def prepare_promotions(self, obj):
        promotions = []
        for promotion in obj.assigned_promotions():
            try:
                promotions.append(promotion._meta.verbose_name.title())
            except:
                promotions.append('*Noname*')
        return ",".join(promotions)

    def prepare_balance_total_usd(self, obj):
        balance = obj.get_ballance()
        return balance['USD']['paid']

    def prepare_balance_total_inr(self, obj):
        balance = obj.get_ballance()
        return balance['INR']['paid']

    def prepare_balance_year_usd(self, obj):
        balance = obj.get_ballance()
        return balance['USD']['donated_year']

    def prepare_balance_year_inr(self, obj):
        balance = obj.get_ballance()
        return balance['INR']['donated_year']

    def prepare_balance_financial_year_usd(self, obj):
        balance = obj.get_ballance()
        return balance['USD']['donated_financial_year']

    def prepare_balance_financial_year_inr(self, obj):
        balance = obj.get_ballance()
        return balance['INR']['donated_financial_year']

    def get_model(self):
        return Person

    # def index_queryset(self, using=None):
    #     """Used when the entire index for model is updated."""
    #     return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())


class PersonSearchIndexMixin(indexes.SearchIndex):
    full_name = indexes.CharField(model_attr='person__full_name')
    mixed_name = indexes.CharField()
    initiated_name = indexes.CharField(model_attr='person__initiated_name')
    first_name = indexes.CharField(model_attr='person__first_name')
    middle_name = indexes.CharField(model_attr='person__last_name')
    last_name = indexes.CharField(model_attr='person__last_name')
    email = indexes.CharField(model_attr='person__email')
    phone_number = indexes.CharField(model_attr='person__phone_number')
    yatra = indexes.CharField(model_attr='person__get_yatra_display',
                              faceted=True)
    address = indexes.CharField(model_attr='person__address')
    city = indexes.CharField(model_attr='person__city')
    state = indexes.CharField(model_attr='person__state')
    country = indexes.CharField(model_attr='person__get_country_display', faceted=True)
    zone = indexes.CharField(faceted=True)
    postcode = indexes.CharField(model_attr='person__postcode')
    pan_card_number = indexes.CharField(model_attr='person__pan_card_number')

    def prepare_mixed_name(self, obj):
        return obj.person.join_fields(
            ('initiated_name', 'first_name', 'middle_name', 'last_name'),
            separator=" ").replace('.', '. ').replace('-', ' ')

    def prepare_yatra(self, obj):
        if obj.person.yatra:
            return obj.person.get_yatra_display()
        else:
            return 'None'

    def prepare_zone(self, obj):
        if obj.person.country in COUNTRIES_TO_ZONES:
            return COUNTRIES_TO_ZONES[obj.person.country]
        else:
            return 'No Zone'


class PledgePersonSearchIndexMixin(indexes.SearchIndex):
    full_name = indexes.CharField(model_attr='pledge__person__full_name')
    mixed_name = indexes.CharField()
    initiated_name = indexes.CharField(model_attr='pledge__person__initiated_name')
    first_name = indexes.CharField(model_attr='pledge__person__first_name')
    middle_name = indexes.CharField(model_attr='pledge__person__last_name')
    last_name = indexes.CharField(model_attr='pledge__person__last_name')
    email = indexes.CharField(model_attr='pledge__person__email')
    phone_number = indexes.CharField(model_attr='pledge__person__phone_number')
    yatra = indexes.CharField(model_attr='pledge__person__get_yatra_display',
                              faceted=True)
    address = indexes.CharField(model_attr='pledge__person__address')
    city = indexes.CharField(model_attr='pledge__person__city')
    state = indexes.CharField(model_attr='pledge__person__state')
    country = indexes.CharField(model_attr='pledge__person__get_country_display', faceted=True)
    zone = indexes.CharField(faceted=True)
    postcode = indexes.CharField(model_attr='pledge__person__postcode')
    pan_card_number = indexes.CharField(model_attr='pledge__person__pan_card_number')

    def prepare_mixed_name(self, obj):
        return obj.pledge.person.join_fields(
            ('initiated_name', 'first_name', 'middle_name', 'last_name'),
            separator=" ").replace('.', '. ').replace('-', ' ')

    def prepare_yatra(self, obj):
        if obj.pledge.person.yatra:
            return obj.pledge.person.get_yatra_display()
        else:
            return 'None'

    def prepare_zone(self, obj):
        if obj.pledge.person.country in COUNTRIES_TO_ZONES:
            return COUNTRIES_TO_ZONES[obj.pledge.person.country]
        else:
            return 'No Zone'
