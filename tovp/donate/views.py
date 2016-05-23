from django.views.generic.base import TemplateView


class DonateView(TemplateView):
    template_name = "donate/donate.html"

    def get_context_data(self, **kwargs):
        context = super(DonateView, self).get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context
