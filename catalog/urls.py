from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductsList.as_view(), name='catalog'),
    path('<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
]
