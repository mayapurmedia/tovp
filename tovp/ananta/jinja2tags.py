from __future__ import absolute_import

import jinja2
from jinja2.ext import Extension

from django.utils.timesince import timesince, timeuntil
from django.core.urlresolvers import reverse

from .templatetags.pagination_tags import paginate_list, pager
from .templatetags.core_tags import (add_css, format_date, update_url_query,
                                     format_with_commas, format_for_india,
                                     format_currency, num2words, makeplain,
                                     active_link_class, now)


class PaginationExtension(Extension):
    def __init__(self, environment):
        super(PaginationExtension, self).__init__(environment)

        self.environment.globals.update({
            'paginate_list': jinja2.contextfunction(paginate_list),
            'pager': jinja2.contextfunction(pager),
        })


class CoreExtension(Extension):
    def _url_reverse(self, name, *args, **kwargs):
        return reverse(name, args=args, kwargs=kwargs)

    def __init__(self, environment):
        super(CoreExtension, self).__init__(environment)
        environment.filters["timesince"] = timesince
        environment.filters["timeuntil"] = timeuntil

        environment.filters["add_css"] = add_css
        environment.filters["format_date"] = format_date
        environment.filters["update_url_query"] = update_url_query
        environment.filters["format_with_commas"] = format_with_commas
        environment.filters["format_for_india"] = format_for_india
        environment.filters["num2words"] = num2words
        environment.filters["makeplain"] = makeplain
        environment.filters["now"] = now

        environment.globals["active_link_class"] = active_link_class
        environment.globals["format_currency"] = format_currency
        environment.globals["now"] = now
        environment.globals["url"] = self._url_reverse



# Nicer import names
pagination = PaginationExtension
core = CoreExtension
