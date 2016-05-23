from search.views import SearchView

from .forms import SearchForm


class DonorList(SearchView):
    form_class = SearchForm
    paginate_by = 90
    template_name = "donor_list/results.html"
    show_form = None

    def default_faceted_by_secondary(self):
        return {
            "followed_by": None,
            "currency": None,
            "status": None,
            "source": None,
            "yatra": None,
            "country": None,
            "promotion_type": None,
        }
