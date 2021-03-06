from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.apps import apps
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from attachments.models import Attachment
from attachments.forms import AttachmentForm


def add_url_for_obj(obj):
    return reverse('add_attachment', kwargs={
        'app_label': obj._meta.app_label,
        'model_name': obj._meta.model_name,
        'pk': obj.pk
    })


@login_required
def add_attachment(request, app_label, model_name, pk,
                   template_name='attachments/add.html', extra_context={}):

    model = apps.get_model(app_label, model_name)
    if model is None:
        return HttpResponseRedirect(next)
    obj = get_object_or_404(model, pk=pk)

    next = request.POST.get('next', obj.get_absolute_url())
    if not request.POST:
        form = AttachmentForm()
    else:
        form = AttachmentForm(request.POST, request.FILES)

    if form.is_valid():
        form.save(request, obj)
        messages.success(request, ugettext('Your attachment was uploaded.'))
        return HttpResponseRedirect(next)
    else:
        template_context = {
            'form': form,
            'form_url': add_url_for_obj(obj),
            'next': next,
        }
        template_context.update(extra_context)
        return render(request, template_name, template_context)


@login_required
def delete_attachment(request, attachment_pk):
    g = get_object_or_404(Attachment, pk=attachment_pk)
    if request.user.has_perm('delete_foreign_attachments') \
       or request.user == g.creator:
        g.delete()
        messages.success(request, ugettext('Your attachment was deleted.'))
    next = request.REQUEST.get('next') or '/'
    return HttpResponseRedirect(next)
