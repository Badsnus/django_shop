from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContactsMain.as_view(), name='contacts'),
]
