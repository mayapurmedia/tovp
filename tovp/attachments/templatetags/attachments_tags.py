from django import template
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse

import jinja2

from ..forms import AttachmentForm
from ..models import Attachment
from ..views import add_url_for_obj


register = template.Library()


@register.tag(name="active_link_class")
def get_attachments_for(obj):
    return Attachment.objects.attachments_for_object(obj)


@register.tag(name="get_add_attachments_url_for")
def get_add_attachments_url_for(obj):
    return add_url_for_obj(obj)


@jinja2.contextfunction
@register.tag(name="attachment_form")
def attachment_form(context, request, obj):
    """
    Renders a "upload attachment" form.

    The user must own ``attachments.add_attachment permission`` to add
    attachments.
    """

    if context['user'].has_perm('attachments.add_attachment'):
        return render_to_string('attachments/add_form.html', {
            'form': AttachmentForm(),
            'form_url': add_url_for_obj(obj),
            'next': context['request'].build_absolute_uri(),
            'csrf_cookie': request.COOKIES['csrftoken']
        })
    else:
        return ''


@jinja2.contextfunction
@register.tag(name="attachment_delete_link")
def attachment_delete_link(context, attachment):
    """
    Renders a html link to the delete view of the given attachment. Returns
    no content if the request-user has no permission to delete attachments.

    The user must own either the ``attachments.delete_attachment`` permission
    and is the creator of the attachment, that he can delete it or he has
    ``attachments.delete_foreign_attachments`` which allows him to delete all
    attachments.
    """
    if context['user'].has_perm('delete_foreign_attachments') \
       or (context['user'] == attachment.creator and
           context['user'].has_perm('attachments.delete_attachment')):
        return render_to_string('attachments/add_form.html', {
            'next': context['request'].build_absolute_uri(),
            'delete_url': reverse('delete_attachment',
                                  kwargs={'attachment_pk': attachment.pk})
        })
    return ''
