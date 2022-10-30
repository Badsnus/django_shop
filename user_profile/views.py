from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, FormView, LogoutView
from django.db.models import F
from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic

from . import forms
from .models import Cart, Product


class ProfilePage(generic.ListView):
    template_name = 'user_profile/index.html'
    extra_context = {}

    #
    def get_context_data(self, *, object_list=None, **kwargs):
        print(self.extra_context)
        self.extra_context['total_count'] = (
            self.extra_context['products'][0]['count']
        )
        self.extra_context['total_price'] = (
            self.extra_context['products'][0]['price']
        )

        return self.extra_context

    def get_queryset(self):
        products = list(Cart.objects.values(
            'items__name', 'items__description', 'items__price', 'items__img',
            'count', 'price'
        ).filter(user=self.request.user))
        self.extra_context['products'] = products
        return products

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
            Cart.objects.create(user=user)
            return redirect('profile')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class ProfileLogout(LogoutView):
    next_page = '/profile/login/'


class AddCartItem(generic.View):

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('/profile/login')

        product = get_object_or_404(Product, pk=kwargs['pk'])
        cart = Cart.objects.filter(user=request.user)
        cart.update(count=F('count') + 1,
                    price=F('price') + product.price)
        cart = cart.get()
        cart.items.add(product)
        return redirect(f'/catalog/{kwargs["pk"]}/')


class DeleteCartItem(generic.View):
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('/profile/login')
        product = get_object_or_404(Product, pk=kwargs['pk'])
        cart = Cart.objects.filter(user=request.user)
        cart.update(count=F('count') - 1,
                    price=F('price') - product.price)
        cart = cart.get()
        cart.items.remove(product)
        return redirect(f'/catalog/{kwargs["pk"]}/')
