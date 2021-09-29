from django.urls import path, include
from django.contrib import admin
from . import views
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('beaches',views.BeachView, 'beach')
# router.register('posts',views.PostView, 'post')


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
    path('beach/', views.BeachList.as_view(), name='beach_list'),
    path('beach/<int:pk>', views.BeachDetail.as_view(), name = 'beach_detail'),
    path('post/', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>', views.PostDetail.as_view(), name = 'post_detail'),
    # path('post/edit/<int:pk>', views.PostEdit.as_view(), name = 'post_edit'),
    # path('post/delete/<int:pk>', views.PostDelete.as_view(), name = 'post_delete'),
]
