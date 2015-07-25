from haystack import indexes

from ananta.search_indexes import ContentSearchIndexMixin

from .models import Gift


class GiftIndex(ContentSearchIndexMixin, indexes.SearchIndex,
                indexes.Indexable):
    content_name = 'Gift'
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    description = indexes.CharField(model_attr='description')

    def get_model(self):
        return Gift

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


# class PersonSearchIndexMixin(indexes.SearchIndex):
#     full_name = indexes.CharField(model_attr='person__full_name')
#     mixed_name = indexes.CharField()
#     initiated_name = indexes.CharField(model_attr='person__initiated_name')
#     first_name = indexes.CharField(model_attr='person__first_name')
#     middle_name = indexes.CharField(model_attr='person__last_name')
#     last_name = indexes.CharField(model_attr='person__last_name')
#     email = indexes.CharField(model_attr='person__email')
#     phone_number = indexes.CharField(model_attr='person__phone_number')
#     yatra = indexes.CharField(model_attr='person__get_yatra_display',
#                               faceted=True)
#     address = indexes.CharField(model_attr='person__address')
#     city = indexes.CharField(model_attr='person__city')
#     state = indexes.CharField(model_attr='person__state')
#     country = indexes.CharField(model_attr='person__get_country_display', faceted=True)
#     postcode = indexes.CharField(model_attr='person__postcode')
#     pan_card_number = indexes.CharField(model_attr='person__pan_card_number')

#     def prepare_mixed_name(self, obj):
#         return obj.person.join_fields(
#             ('initiated_name', 'first_name', 'middle_name', 'last_name'),
#             separator=" ").replace('.', '. ').replace('-', ' ')

#     def prepare_yatra(self, obj):
#         if obj.person.yatra:
#             return obj.person.get_yatra_display()
#         else:
#             return 'None'


# class PledgePersonSearchIndexMixin(indexes.SearchIndex):
#     full_name = indexes.CharField(model_attr='pledge__person__full_name')
#     mixed_name = indexes.CharField()
#     initiated_name = indexes.CharField(model_attr='pledge__person__initiated_name')
#     first_name = indexes.CharField(model_attr='pledge__person__first_name')
#     middle_name = indexes.CharField(model_attr='pledge__person__last_name')
#     last_name = indexes.CharField(model_attr='pledge__person__last_name')
#     email = indexes.CharField(model_attr='pledge__person__email')
#     phone_number = indexes.CharField(model_attr='pledge__person__phone_number')
#     yatra = indexes.CharField(model_attr='pledge__person__get_yatra_display',
#                               faceted=True)
#     address = indexes.CharField(model_attr='pledge__person__address')
#     city = indexes.CharField(model_attr='pledge__person__city')
#     state = indexes.CharField(model_attr='pledge__person__state')
#     country = indexes.CharField(model_attr='pledge__person__get_country_display', faceted=True)
#     postcode = indexes.CharField(model_attr='pledge__person__postcode')
#     pan_card_number = indexes.CharField(model_attr='pledge__person__pan_card_number')

#     def prepare_mixed_name(self, obj):
#         return obj.pledge.person.join_fields(
#             ('initiated_name', 'first_name', 'middle_name', 'last_name'),
#             separator=" ").replace('.', '. ').replace('-', ' ')

#     def prepare_yatra(self, obj):
#         if obj.pledge.person.yatra:
#             return obj.pledge.person.get_yatra_display()
#         else:
#             return 'None'
