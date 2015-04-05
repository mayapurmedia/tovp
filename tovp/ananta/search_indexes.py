from haystack import indexes


class ContentSearchIndexMixin(indexes.SearchIndex):
    record_id = indexes.IntegerField(model_attr='pk')
    created = indexes.DateTimeField(model_attr='created')
    modified = indexes.DateTimeField(model_attr='modified')
    absolute_url = indexes.CharField(model_attr='get_absolute_url')
    content_type = indexes.CharField(faceted=True)
    created_by = indexes.CharField(faceted=True)
    modified_by = indexes.CharField(faceted=True)

    def prepare_content_type(self, obj):
        try:
            return self.content_name
        except:
            return 'Noname'

    def prepare_created_by(self, obj):
        if obj.created_by:
            return obj.created_by.display_name

    def prepare_modified_by(self, obj):
        if obj.modified_by:
            return obj.modified_by.display_name
