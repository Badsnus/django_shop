from django.contrib.auth import authenticate, login
from django.views import generic
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, FormView, LogoutView

from . import forms


class ProfilePage(generic.TemplateView):
    template_name = 'user_profile/index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        return redirect('login/')


class ProfileLogin(LoginView):
    template_name = 'user_profile/login.html'
    form_class = forms.LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return super().get(request, *args, **kwargs)
        return redirect('/profile/')


class ProfileRegistration(FormView):
    form_class = forms.RegisterForm
    template_name = 'user_profile/registration.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return super().get(request, *args, **kwargs)
        return redirect('/profile/')

    def post(self, request, *args, **kwargs):
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class ProfileLogout(LogoutView):
    next_page = '/profile/login/'
