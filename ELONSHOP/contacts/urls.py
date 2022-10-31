from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContactsView.as_view(), name='contacts'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
    path('error/', views.ErrorView.as_view(), name='error'),
]
