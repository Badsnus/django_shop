from django.views.generic import TemplateView


class ContactsMain(TemplateView):
    template_name = 'contacts/index.html'
