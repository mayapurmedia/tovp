from haystack.signals import RealtimeSignalProcessor


class RelatedRealtimeSignalProcessor(RealtimeSignalProcessor):
    def handle_save(self, sender, instance, **kwargs):
        if hasattr(instance, 'reindex_related'):
            for related in instance.reindex_related():
                self.handle_save(related.__class__, related)
        return super(RelatedRealtimeSignalProcessor, self). \
            handle_save(sender, instance, **kwargs)

    def handle_delete(self, sender, instance, **kwargs):
        if hasattr(instance, 'reindex_related'):
            for related in instance.reindex_related():
                self.handle_delete(related.__class__, related)
        return super(RelatedRealtimeSignalProcessor, self). \
            handle_delete(sender, instance, **kwargs)
