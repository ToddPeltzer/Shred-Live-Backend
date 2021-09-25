from rest_framework import serializers
from .models import Beach, Post

class BeachSerializer(serializers.HyperlinkedModelSerializer):
    # posts = serializers.HyperlinkedRelatedField(
    #     view_name = 'post_detail',
    #     many = True,
    #     read_only = True
    # )
    # beach_url = serializers.ModelSerializer.serializer_url_field(
    #     view_name = 'beach_detail'
    # )
    class Meta:
        model = Beach
        fields = ('id', 'name', 'image_url', 'description', 'city', 'state')


class PostSerializer(serializers.ModelSerializer):
    # beach = serializers.HyperlinkedRelatedField(
    #     view_name = 'beach_detail',
    #     read_only = True
    # )
    # beach_id = serializers.PrimaryKeyRelatedField(
    #     queryset = Beach.objects.all(),
    #     source = 'beach'
    # )
    class Meta:
        model = Post
        fields = ('user', 'body', 'date', 'image', 'beach')