from haystack import indexes


class ContentSearchIndexMixin(indexes.SearchIndex):
    record_id = indexes.IntegerField(model_attr='pk')
    created = indexes.DateTimeField(model_attr='created')
    modified = indexes.DateTimeField(model_attr='modified')
    absolute_url = indexes.CharField(model_attr='get_absolute_url')
    content_type = indexes.CharField(faceted=True)

    def prepare_content_type(self, obj):
        try:
            return self.content_name
        except:
            return 'Noname'
