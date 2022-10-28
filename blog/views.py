from django.views.generic import TemplateView


class BlogMain(TemplateView):
    template_name = 'blog/index.html'
