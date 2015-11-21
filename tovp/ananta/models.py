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
        (u'tovp-f-mayapur', _('TOVP Fundraising Mayapur')),
        (u'nityananda', _('Nityananda Tour')),
        (u'jps-office', _('JPS Office')),
        (u'namahatta', _('JPS Namahatta')),
        (u'jps-others', _('JPS Others')),
        (u'gkg-vp-2015', _('GKG Vyasa Puja 2015')),
        (u'bcs-vp-2015', _('BCS Vyasa Puja 2015')),
        (u'vvps-vp-2015', _('Vedavyasapriya Swami Vyasa Puja 2015')),
        (u'rns-kartik-yatra', _('RNS Kartik Yatra')),
        (u'j-w-marriot', _('J W Marriot')),
        (u'kanjurmarg-mumbai-2015', _('Kanjurmarg Mumbai 2015')),
        (u'nvs', _('Nava Yogendra Swami')),
        (u'mso', _('MSO')),
        (u'lm-reception', _('Life Membership Reception')),
        (u'vrindavan-booth', _('Vrindavan Booth')),
        (u'prabhupada-currency-inr', _('Prabhupada Currency INR')),
        (u'other', _('Other')),
    )
    source = models.CharField("Source", max_length=30, default='',
                              choices=SOURCE_CHOICES, blank=True)

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
