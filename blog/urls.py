from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogMain.as_view(), name='blog'),
]
