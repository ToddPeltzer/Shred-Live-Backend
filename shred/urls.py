from django.urls import path
from . import views

urlpatterns = [
    path('', views.BeachList.as_view(), name='beach_list'),
]
