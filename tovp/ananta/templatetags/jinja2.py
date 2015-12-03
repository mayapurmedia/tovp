from __future__ import absolute_import

# import jinja2
from jinja2.ext import Extension

from .core_tags import (add_css, format_date, update_url_query,
                        format_with_commas, format_for_india, num2words,
                        makeplain, active_link_class)


class CoreExtension(Extension):
    def __init__(self, environment):
        super(CoreExtension, self).__init__(environment)
        environment.filters["add_css"] = add_css
        environment.filters["format_date"] = format_date
        environment.filters["update_url_query"] = update_url_query
        environment.filters["format_with_commas"] = format_with_commas
        environment.filters["format_for_india"] = format_for_india
        environment.filters["num2words"] = num2words
        environment.filters["makeplain"] = makeplain

        environment.globals["active_link_class"] = active_link_class

# Nicer import name
core = CoreExtension
