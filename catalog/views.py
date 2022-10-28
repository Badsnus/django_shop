from django.views.generic import TemplateView


class CatalogMain(TemplateView):
    template_name = 'catalog/index.html'
