from django.views.generic import RedirectView
from django.shortcuts import redirect, reverse

from .utils import bot


class SendMessageInAdminChannel(RedirectView):
    pattern_name = 'thanks'

    def post(self, request, *args, **kwargs):
        username = request.POST.get('telegram', None)
        question = request.POST.get('question', None)
        if username and question:
            bot.send(username, question)
            return super().post(request, *args, **kwargs)
        return redirect(reverse('error'))
