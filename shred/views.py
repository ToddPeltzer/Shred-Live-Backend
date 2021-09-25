from rest_framework import generics
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
    queryset = Post.objects.all()
    serializer_class = PostSerializer