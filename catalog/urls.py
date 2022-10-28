from django.urls import path

from . import views

urlpatterns = [
    path('', views.CatalogMain.as_view(), name='catalog'),
]
