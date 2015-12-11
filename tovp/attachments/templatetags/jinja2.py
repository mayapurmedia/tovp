from __future__ import absolute_import

# import jinja2
from jinja2.ext import Extension

from .attachments_tags import (get_attachments_for, get_add_attachments_url_for,
                               attachment_form, attachment_delete_link)


class AttachmentsExtension(Extension):
    def __init__(self, environment):
        super(AttachmentsExtension, self).__init__(environment)

        environment.globals["get_attachments_for"] = get_attachments_for
        environment.globals["get_add_attachments_url_for"] = get_add_attachments_url_for
        environment.globals["attachment_form"] = attachment_form
        environment.globals["attachment_delete_link"] = attachment_delete_link

# Nicer import name
attachments = AttachmentsExtension
