from rest_framework import serializers
from .models import Beach, Post

class BeachSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Beach
        fields = ('id', 'name', 'image_url', 'description', 'city', 'state')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'body', 'date', 'image', 'beach')
