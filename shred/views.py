from rest_framework import generics
from .serializers import BeachSerializer
from .models import Beach

# Create your views here.

class BeachList(generics.ListCreateAPIView):
    queryset = Beach.objects.all()
    serializer_class = BeachSerializer