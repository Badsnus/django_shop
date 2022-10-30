from django.views import generic
from django.shortcuts import redirect, HttpResponse, get_object_or_404
from django.db.models import Q

from .models import Product


class ProductsList(generic.ListView):
    template_name = 'catalog/index.html'
    model = Product

    def get_queryset(self):
        search = self.request.GET.get('search')
        reverse, sort_by = '', self.request.GET.get('sort_by', 'name')
        favourite = self.request.GET.get('favourite')

        if '_' in sort_by:
            reverse, sort_by = '+', sort_by.split('_')[0]
        if sort_by not in {'name', 'price', 'priceD'}:
            sort_by = 'name'
        if favourite:
            queryset = Product.objects.filter(
                favourite__username=self.request.user)
        else:
            queryset = Product.objects.all()

        if not search:
            queryset = queryset.order_by(sort_by)
        else:
            queryset = queryset.filter(
                Q(name__contains=search) |
                Q(description__contains=search)).order_by(sort_by)
        if reverse:
            queryset = queryset.reverse()
        self.extra_context = dict(search=search, favourite=favourite,
                                  sort_by=reverse + sort_by)
        return queryset


class ProductDetail(generic.DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['in_fav'] = self.object.in_favourite(self.request.user)
        context['auth_error'] = self.request.GET.get('noauth', False)
        return context

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect(f'/catalog/{kwargs["pk"]}/?noauth=1')
        product = get_object_or_404(Product, pk=kwargs['pk'])
        if product.favourite.filter(
                favourite__favourite__username=request.user):
            product.favourite.remove(request.user)
        else:
            product.favourite.add(request.user)

        return redirect(f'/catalog/{kwargs["pk"]}/')
