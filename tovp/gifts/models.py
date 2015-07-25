from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel
from model_utils.fields import MonitorField, StatusField
from model_utils import Choices
from audit_log.models import AuthStampedModel

from ananta.models import NextPrevMixin
from contacts.models import Person


class Gift(AuthStampedModel, NextPrevMixin, TimeStampedModel):
    name = models.CharField(max_length=100,
                            help_text=_('Enter gift name.'))
    description = models.TextField(blank=True)

    @permalink
    def get_absolute_url(self):
        return ('gifts:gift:detail', None, {'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class GiftGiven(AuthStampedModel, NextPrevMixin, TimeStampedModel):
    person = models.ForeignKey(Person, verbose_name="Person",
                               related_name='gifts')
    gift = models.ForeignKey(Gift, verbose_name="Gift", related_name='gifts')

    STATUS = Choices(
        ('sent', _('Sent')),
        ('returned', _('Returned')),
        ('delivered', _('Delivered')),
    )
    status = StatusField()
    status_changed = MonitorField(monitor='status')

    note = models.TextField(_("Note"), blank=True)

    @permalink
    def get_absolute_url(self):
        return ('gifts:gift_given:detail', None, {'pk': self.pk})

    def __str__(self):
        return '%s for %s' % (self.gift.name, self.person.mixed_name)
