from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('<pk>/', views.PostDetail.as_view(),
            name='post_detail'),
    # path('like_post/<pk>/', views.LikePost.as_view(),
    #      name='like_post'),
]
