from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.ProfilePage.as_view(), name='profile'),
    path('login/', views.ProfileLogin.as_view(), name='login'),
    path('registration', views.ProfileRegistration.as_view(), name='reg'),
    path('logout/', views.ProfileLogout.as_view(), name='logout'),
    # path('', include('django.contrib.auth.urls'))
]
