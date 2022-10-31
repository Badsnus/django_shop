from django.views.generic import TemplateView


class ContactsView(TemplateView):
    template_name = 'contacts/index.html'


class ThanksView(TemplateView):
    template_name = 'contacts/thanks.html'


class ErrorView(TemplateView):
    template_name = 'contacts/error.html'
