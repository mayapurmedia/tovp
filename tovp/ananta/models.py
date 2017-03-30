from django.db import models
from django.utils.translation import ugettext_lazy as _
from reversion.views import RevisionMixin

from .utils import revision_set_comment


class RevisionCommentMixin(RevisionMixin):
    def form_valid(self, form):
        revision_set_comment(form)
        return super(RevisionCommentMixin, self).form_valid(form)

    class Meta:
        abstract = True


class NextPrevMixin(object):
    def next(self):
        obj = self.__class__.objects.filter(pk__gt=self.pk)[0:1]
        if len(obj):
            return obj[0]
        return ''

    def prev(self):
        obj = self.__class__.objects.filter(pk__lt=self.pk).order_by('-pk')[0:1]
        if len(obj):
            return obj[0]
        return ''
