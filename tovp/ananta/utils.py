from django.utils.text import get_text_list
from django.utils.encoding import force_text
from django.utils.translation import ugettext as _

from reversion import set_comment


def revision_set_comment(form, formsets=None):
    """
    Sets comment for revision based on changed fields
    """
    change_message = []
    if form.changed_data:
        change_message.append(_('Changed %s.')
                              % get_text_list(form.changed_data, _('and')))

    if formsets:
        for formset in formsets:
            for added_object in formset.new_objects:
                change_message.append(
                    _('Added %(name)s "%(object)s".')
                    % {'name': force_text(added_object._meta.verbose_name),
                       'object': force_text(added_object)})
            for changed_object, changed_fields in formset.changed_objects:
                change_message.append(
                    _('Changed %(list)s for %(name)s "%(object)s".')
                    % {'list': get_text_list(changed_fields, _('and')),
                       'name': force_text(changed_object._meta.verbose_name),
                       'object': force_text(changed_object)})
            for deleted_object in formset.deleted_objects:
                change_message.append(
                    _('Deleted %(name)s "%(object)s".')
                    % {'name': force_text(deleted_object._meta.verbose_name),
                       'object': force_text(deleted_object)})
    change_message = ' '.join(change_message)
    set_comment(
        change_message or _('No fields changed.'))
