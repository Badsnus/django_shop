from django.urls import path

from . import views

urlpatterns = [
    path('', views.SendMessageInAdminChannel.as_view(), name='send_message'),
]
