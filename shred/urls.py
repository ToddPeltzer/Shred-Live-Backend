from django.urls import path
from . import views

urlpatterns = [
    path('beach/', views.BeachList.as_view(), name='beach_list'),
    path('post/', views.PostList.as_view(), name='post_list'),
]
