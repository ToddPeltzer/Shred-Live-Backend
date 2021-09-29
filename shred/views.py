from rest_framework import generics, permissions, viewsets
from .serializers import BeachSerializer, PostSerializer
from .models import Beach, Post


# Create your views here.

class BeachList(generics.ListCreateAPIView):
    queryset = Beach.objects.all()
    serializer_class = BeachSerializer


class BeachDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Beach.objects.all()
    serializer_class = BeachSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.AllowAny)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# THESE TWO DONT WORK
# class PostEdit(generics.UpdateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

# class PostDelete(generics.RetrieveDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticated]  
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
# 

# class BeachView(viewsets.ModelViewSet):
#     serializer_class = BeachSerializer
#     queryset = Beach.objects.all()

# class PostView(viewsets.ModelViewSet):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()