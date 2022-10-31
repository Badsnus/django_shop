from django.contrib.auth import authenticate, login, views
from django.db import transaction, models
from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.views import generic

from send_message.utils import bot
from . import forms
from .models import Cart, Product


class ProfilePage(generic.ListView):
    template_name = 'user_profile/index.html'
    extra_context = {}

    def get_context_data(self, *, object_list=None, **kwargs):
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
            'items__pk', 'count', 'price'
        ).filter(user=self.request.user))
        self.extra_context['products'] = products
        self.extra_context['have'] = products[0]['items__name']
        return products

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        return redirect('login/')


class ProfileLogin(views.LoginView):
    template_name = 'user_profile/login.html'
    form_class = forms.LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return super().get(request, *args, **kwargs)
        return redirect('/profile/')

    def form_valid(self, form):
        login(self.request, form.get_user())
        # if user was created in admin panel we need to add cart for him
        Cart.objects.get_or_create(user=self.request.user)
        return redirect(self.get_success_url())


class ProfileRegistration(views.FormView):
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


class ProfileLogout(views.LogoutView):
    next_page = '/profile/login/'


class OrderView(generic.TemplateView):
    template_name = 'user_profile/order_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_price'] = Cart.objects.values('price').get(
            user=self.request.user)['price']
        return context

    def post(self, request, *args, **kwargs):
        telegram = request.POST.get('telegram')
        return redirect(reverse('fake_payment') + f'?telegram={telegram}')


class FakePaymentView(generic.TemplateView):
    template_name = 'user_profile/fake_payment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['telegram'] = self.request.GET.get('telegram')
        return context

    def post(self, request, *args, **kwargs):
        telegram = request.POST.get('telegram')
        cart = Cart.objects.values('price', 'items__name',
                                   'items__price').filter(
            user=request.user)
        cart = Cart.objects.prefetch_related('items').get(user=request.user)
        bot.order(telegram, cart.price, cart.items.all())
        cart.items.clear()
        cart.price = 0
        cart.count = 0
        cart.save()
        return redirect(reverse('success_order'))


class SuccessOrderView(generic.TemplateView):
    template_name = 'user_profile/success_order.html'


class AddCartItem(generic.View):
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('/profile/login')
        product = get_object_or_404(Product, pk=kwargs['pk'])
        cart = Cart.objects.filter(user=request.user)
        with transaction.atomic():
            cart.update(count=models.F('count') + 1,
                        price=models.F('price') + product.price)
            cart = cart.get()
            cart.items.add(product)
        return redirect(f'/catalog/{kwargs["pk"]}/')


class DeleteCartItem(generic.View):
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('/profile/login')
        product = get_object_or_404(Product, pk=kwargs['pk'])
        cart = Cart.objects.filter(user=request.user)
        with transaction.atomic():
            cart.update(count=models.F('count') - 1,
                        price=models.F('price') - product.price)
            cart = cart.get()
            cart.items.remove(product)
        redirect_to = request.GET.get('redirect', f'/catalog/{kwargs["pk"]}/')
        return redirect(redirect_to)
