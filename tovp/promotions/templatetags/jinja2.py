from __future__ import absolute_import

# import jinja2
from jinja2.ext import Extension

from .promotions_tags import promo_ballance


class PromotionsExtension(Extension):
    def __init__(self, environment):
        super(PromotionsExtension, self).__init__(environment)
        environment.filters["promo_ballance"] = promo_ballance

# Nicer import name
promotions = PromotionsExtension
