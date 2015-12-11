# import re
from jingo import register
from jinja2 import Markup
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.shortcuts import render
from django.template.loader import render_to_string


@register.function
def paginate_list(request, object_list, items_per_page=8):
    '''
    Returns paginated list
    '''

    paginator = Paginator(object_list, items_per_page)

    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        items = paginator.page(paginator.num_pages)

    return items


@register.function
def pager(request, paginated_objects, css_classes=None, align='pagination-centered'):
    '''
    Renders pagination pager
    '''

    return Markup(render_to_string('jingo_paginator/pager.jinja', {"request": request, "pager": paginated_objects, "align": align}))
