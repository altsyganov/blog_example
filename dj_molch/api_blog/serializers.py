from rest_framework import serializers

from .models import Post, Tag


class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = ['url', 'title', 'slug', 'body', 'tags']


class TagSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tag
        fields = ['url', 'tag', 'slug']
