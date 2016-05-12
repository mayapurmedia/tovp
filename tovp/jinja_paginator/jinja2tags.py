from __future__ import absolute_import

import jinja2
from jinja2.ext import Extension

from .templatetags.jinja_paginator_tags import paginate_list, pager


class PaginationExtension(Extension):
    def __init__(self, environment):
        super(PaginationExtension, self).__init__(environment)

        self.environment.globals.update({
            'paginate_list': jinja2.contextfunction(paginate_list),
            'pager': jinja2.contextfunction(pager),
        })


core = PaginationExtension
