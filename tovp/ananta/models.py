from django.db import models
from django.utils.translation import ugettext_lazy as _

from .utils import revision_set_comment


class RevisionCommentMixin(object):
    def form_valid(self, form):
        revision_set_comment(form)
        return super(RevisionCommentMixin, self).form_valid(form)

    class Meta:
        abstract = True


class SourceMixin(models.Model):
    SOURCE_CHOICES = (
        (u'nityananda', _('Nityananda Tour')),
        (u'jps-office', _('JPS Office')),
        (u'namahatta', _('JPS Namahatta')),
        (u'jps-others', _('JPS Others')),
        (u'mso', _('M.S.O.')),
        (u'lm-reception', _('Life Membership Reception')),
        (u'vrindavan-booth', _('Vrindavan')),
        (u'other', _('Other')),
    )
    source = models.CharField("Source", max_length=30, default='',
                              choices=SOURCE_CHOICES, blank=True)

    class Meta:
        abstract = True
