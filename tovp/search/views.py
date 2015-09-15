from urllib.parse import urlencode

from django import forms
from django.conf import settings
from django.core.paginator import Paginator, InvalidPage
from django.http import Http404
from django.utils.translation import ugettext as _

from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.edit import FormMixin

from braces.views import LoginRequiredMixin
from haystack.query import SearchQuerySet

from contacts.exports import ContactExport
from contributions.exports import PledgeExport, ContributionExport

from .forms import SearchForm, FollowUpForm


class SearchView(LoginRequiredMixin, TemplateResponseMixin, FormMixin, View):
    searchqueryset = SearchQuerySet()
    export_csv = None
    load_all = True
    paginate_by = 36
    allow_empty = True
    show_form = True
    form_class = SearchForm
    paginator_class = Paginator
    search_key = 'general_search'
    search_form_used = None

    exporters = {'Contact': ContactExport,
                 'Contribution': ContributionExport,
                 'Pledge': PledgeExport}

    facets_titles = {
        'content_type': 'Content Type', 'currency': 'Currency',
        'deposited_status': 'Deposited Status', 'promotion_type': 'Promotion Type',
        'status': 'Status', 'payment_method': 'Payment Method',
        'interval': 'Interval', 'country': 'Country', 'yatra': 'Yatra',
        'has_book': 'Book filled', 'has_slip': 'Slip filled',
        'created_by': 'Created By', 'modified_by': 'Modified By',
        'is_external': 'Non Mayapur TOVP Receipt', 'source': 'Source',
        'gifts': 'Has Gift',
    }

    faceted_by_secondary = {
        "deposited_status": None,
        "content_type": None,
        "currency": None,
        "status": None,
        "payment_method": None,
        "source": None,
        "yatra": None,
        "interval": None,
        "country": None,
        "promotion_type": None,
        "has_book": None,
        "has_slip": None,
        "created_by": None,
        "modified_by": None,
        "is_external": None,
        "gifts": None,
    }

    narrow_facets = {
        'first': {
            'title': 'Test 1',
            'has_results': None,
            'fields': (
                'content_type', 'currency', 'status', 'source',
                'deposited_status', 'promotion_type', 'payment_method',
                'yatra', 'interval', 'has_book', 'has_slip', 'created_by',
                'modified_by', 'is_external', 'gifts', 'country',
            ),
        },
    }

    def get_template_names(self):
        return ["search/results.html"]

    def get_searchqueryset(self):
        return self.searchqueryset

    def get_load_all(self):
        return self.load_all

    def get_allow_empty(self):
        """
        Returns ``True`` if the view should display empty lists, and ``False``
        if a 404 should be raised instead.
        """
        return self.allow_empty

    def get_paginate_by(self):
        """
        Get the number of items to paginate by, or ``None`` for no pagination.
        """
        if self.paginate_by is None:
            return getattr(settings, "HAYSTACK_SEARCH_RESULTS_PER_PAGE", 40)
        return self.paginate_by

    def get_paginator(self, results, per_page, orphans=0, allow_empty_first_page=True):
        """
        Return an instance of the paginator for this view.
        """
        return self.paginator_class(results, per_page, orphans=orphans, allow_empty_first_page=allow_empty_first_page)

    def paginate_results(self, results, page_size):
        """
        Paginate the results, if needed.
        """
        paginator = self.get_paginator(results, page_size, allow_empty_first_page=self.get_allow_empty())
        page = self.kwargs.get("page") or self.request.GET.get("page") or 1
        try:
            page_number = int(page)
        except ValueError:
            if page == "last":
                page_number = paginator.num_pages
            else:
                raise Http404(_(u"Page is not 'last', nor can it be converted to an int."))
        try:
            page = paginator.page(page_number)
            return (paginator, page, page.object_list, page.has_other_pages())
        except InvalidPage:
            raise Http404(_(u"Invalid page (%(page_number)s)") % {
                "page_number": page_number
            })

    def get_form_kwargs(self):
        """
        Returns the keyword arguments for instanciating the form.
        """
        kwargs = {
            "initial": self.get_initial(),
            "searchqueryset": self.get_searchqueryset(),
            "load_all": self.get_load_all(),
        }
        if "q" in self.request.GET:
            kwargs.update({
                "data": self.request.GET,
            })
        return kwargs

    def form_valid(self, form):
        results = form.search()

        total_results_count = results.count()
        facets_titles = self.facets_titles
        narrow_facets = self.narrow_facets
        faceted_by_primary = {}
        faceted_by_secondary = self.faceted_by_secondary

        show_primary_filters = None
        show_secondary_filters = None
        show_selected_filters = 0

        for filter_item in faceted_by_primary.keys():
            if filter_item in self.request.GET:
                faceted_by_primary[filter_item] = self.request.GET[filter_item]
                results = results.narrow('%s_exact:"%s"' % (filter_item, self.request.GET[filter_item]))
                show_selected_filters += 1

        for filter_item in faceted_by_secondary.keys():
            if filter_item in self.request.GET:
                faceted_by_secondary[filter_item] = self.request.GET[filter_item]
                # results = results.filter(**{filter_item: self.request.GET[filter_item]})
                if filter_item in ['deposited_status']:
                    results = results.narrow('%s_exact:"%s"' % (filter_item, self.request.GET[filter_item]))
                else:
                    results = results.narrow('%s:"%s"' % (filter_item, self.request.GET[filter_item]))
                show_selected_filters += 1

        page_size = self.get_paginate_by()

        if page_size:

            sort_by_year = None
            active_year_filters = {}

            if sort_by_year:
                results = results.order_by('year')
                show_selected_filters += 1

            facets = results
            # adds main facets
            for filter_item in faceted_by_primary.keys():
                facets = facets.facet(filter_item, order='term')

            # adds secondary facets
            for filter_item in faceted_by_secondary.keys():
                # facets = results.facet("make", order='term').facet("model", order='term').facet("variant", order='term').facet("air_intake", order='term').facet_counts()
                facets = facets.facet(filter_item, order='term')
                # narrow_facets

            facets = facets.facet_counts()

            # ======================================
            if self.export_csv and ('content_type' in self.request.GET):
                if self.request.GET['content_type'] in self.exporters:
                    exporter = self.exporters[self.request.GET['content_type']](results)
                    return exporter.render()
            # ======================================

            paginator, page, results, is_paginated = self.paginate_results(results, page_size)

            # Grumble.
            duped = self.request.GET.copy()
            try:
                del duped["page"]
            except KeyError:
                pass
            query_params = urlencode(duped, doseq=True)

            # process facets and generate form
            filter_form = forms.Form()

            if 'fields' in facets:
                # remove facets which has less then two items
                for facet in faceted_by_secondary:
                    if len(facets['fields'][facet]) < 2:
                        del facets['fields'][facet]
                    else:
                        for topic in narrow_facets:
                            if facet in narrow_facets[topic]['fields']:
                                narrow_facets[topic]['has_results'] = True
                                show_secondary_filters = True
                                continue
        else:
            facets = {}
            query_params = ""
            paginator, page, is_paginated = None, None, False

        content_title = "Search"
        show_export_link = None
        if 'content_type' in self.request.GET and self.request.GET['content_type'] in self.exporters:
            show_export_link = True
        ctx = {
            "form": form,
            "show_form": self.show_form,
            "results": results,
            "page": page,
            "content_title": content_title,
            "paginator": paginator,
            "is_paginated": is_paginated,
            "facets": facets,
            "show_export_link": show_export_link,
            "faceted_by_primary": faceted_by_primary,
            "faceted_by_secondary": faceted_by_secondary,
            "query_params": query_params,
            "filter_form": filter_form,
            "search_form_used": self.search_form_used,
            "show_selected_filters": show_selected_filters,
            "show_primary_filters": show_primary_filters,
            "show_secondary_filters": show_secondary_filters,
            "narrow_facets": narrow_facets,
            "facets_titles": facets_titles,
            "total_results_count": total_results_count,
            "active_year_filters": active_year_filters,
            "meta_description": '',
        }

        return self.render_to_response(self.get_context_data(**ctx))

    def get(self, request, *args, **kwargs):
        self.request = request

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        data = {
        }
        for form_field_id in ['q',
                              'mixed_name',
                              'initiated_name',
                              'first_name',
                              'last_name',
                              'email',
                              'pan_card_number',
                              'phone_number',
                              'serial_number',
                              'book_number',
                              'slip_number',
                              'transaction_id',
                              'postcode',
                              'old_database_id',
                              'record_id',
                              'date_type',
                              'date_from',
                              'date_to',
                              ]:
            if form_field_id in self.request.GET and \
                    self.request.GET[form_field_id]:
                self.search_form_used = True
                data[form_field_id] = self.request.GET[form_field_id]

        if 'export_csv' in self.request.GET and self.request.GET['export_csv']:
            self.export_csv = True

        collector = None
        if 'collector' in self.request.GET and self.request.GET['collector']:
            collector = self.request.GET['collector']

        form = self.form_class(collector, data)
        return self.form_valid(form)


class FollowUpView(SearchView):
    form_class = FollowUpForm
    show_form = None

    faceted_by_secondary = {
        "currency": None,
        "status": None,
        "source": None,
        "yatra": None,
        "country": None,
        "promotion_type": None,
    }
