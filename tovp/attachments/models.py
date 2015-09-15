import os
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel
from audit_log.models import AuthStampedModel


class AttachmentManager(models.Manager):
    def attachments_for_object(self, obj):
        object_type = ContentType.objects.get_for_model(obj)
        return self.filter(content_type__pk=object_type.id,
                           object_id=obj.id)


class Attachment(TimeStampedModel, AuthStampedModel):
    def attachment_upload(instance, filename):
        """Stores the attachment in a "per module/appname/primary key" folder"""
        return 'attachments/%s/%s/%s' % (
            '%s_%s' % (instance.content_object._meta.app_label,
                       instance.content_object._meta.object_name.lower()),
            instance.content_object.pk,
            filename)

    objects = AttachmentManager()

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    attachment_file = models.FileField('attachment', upload_to=attachment_upload)
    description = models.CharField(max_length=255, blank=True)

    ATTACHMENT_TYPE_CHOICES = (
        ('passport', _('Passport')),
        ('cheque', _('Cheque')),
        ('other', _('Other Document')),
    )
    attachment_type = models.CharField(
        "Attachment Type", max_length=100, choices=ATTACHMENT_TYPE_CHOICES)

    class Meta:
        # ordering = ['-created']
        permissions = (
            ('delete_foreign_attachments', 'Can delete foreign attachments'),
        )

    def __str__(self):
        return 'Attached file: %s' % self.attachment_type

    @property
    def filename(self):
        return os.path.split(self.attachment_file.name)[1]
