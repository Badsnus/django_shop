from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.ProfilePage.as_view(), name='profile'),

    path('registration', views.ProfileRegistration.as_view(), name='reg'),
    path('login/', views.ProfileLogin.as_view(), name='login'),
    path('logout/', views.ProfileLogout.as_view(), name='logout'),

    path('order/', views.OrderView.as_view(),
         name='order'),
    path('fake_payment/', views.FakePaymentView.as_view(),
         name='fake_payment'),
    path('success_order/', views.SuccessOrderView.as_view(),
         name='success_order'),

    path('add_cartitem/<int:pk>/', views.AddCartItem.as_view(),
         name='add_item'),
    path('delete_cartitem/<int:pk>/', views.DeleteCartItem.as_view(),
         name='delete_item')
]
