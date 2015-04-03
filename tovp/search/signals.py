from haystack.signals import RealtimeSignalProcessor

class RelatedRealtimeSignalProcessor(RealtimeSignalProcessor):

    def handle_save(self, sender, instance, **kwargs):
        if hasattr(instance, 'reindex_related'):
            for related in instance.reindex_related():
                print(related)
                # related_objects = getattr(instance, related)
                # for related_object in related_objects.all():
                #     print(related_object)
                #     self.handle_save(related_object.__class__, related_object)
                self.handle_save(related.__class__, related)
        return super(RelatedRealtimeSignalProcessor, self).handle_save(sender, instance, **kwargs)

    def handle_delete(self, sender, instance, **kwargs):
        if hasattr(instance, 'reindex_related'):
            for related in instance.reindex_related:
                related_obj = getattr(instance, related)
                self.handle_delete(related_obj.__class__, related_obj)
        return super(RelatedRealtimeSignalProcessor, self).handle_delete(sender, instance, **kwargs)
