from .utils import revision_set_comment


class RevisionCommentMixin(object):
    def form_valid(self, form):
        revision_set_comment(form)
        return super(RevisionCommentMixin, self).form_valid(form)

    class Meta:
        abstract = True
