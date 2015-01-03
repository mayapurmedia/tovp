# -*- coding: utf-8 -*-
'''
Travis-CI Configurations
'''
from .common import Common


class Travis(Common):
    # TEMPLATE_DEBUG has to be True for jingo to call the template_rendered
    # signal which Django's test client uses to save away the contexts for your
    # test to look at later.
    TEMPLATE_DEBUG = True
