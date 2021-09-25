from django.urls import path
from . import views

urlpatterns = [
    path('beach/', views.BeachList.as_view(), name='beach_list'),
    path('beach/<int:pk>', views.BeachDetail.as_view(), name = 'beach_detail'),
    path('post/', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>', views.PostDetail.as_view(), name = 'post_detail'),
]
