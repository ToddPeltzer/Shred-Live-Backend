from rest_framework import serializers
from .models import Beach

class BeachSerializer(serializers.HyperlinkedModelSerializer):
    # posts = serializers.HyperlinkedRelatedField(
    #     view_name = 'post_detail',
    #     many = True,
    #     read_only = True
    # )
    class Meta:
        model = Beach
        fields = ('name', 'image_url', 'description', 'city', 'state')

