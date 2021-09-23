from rest_framework import serializers
from .models import Beach, Post

class BeachSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Beach
        fields = ('name', 'image_url', 'description', 'city', 'state')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('user', 'body', 'date', 'image', 'beach')