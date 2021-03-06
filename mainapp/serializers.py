from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    """ Сериализация постов """
    class Meta:
        model = Post
        fields = ['id', 'post_id', 'title', 'url', 'created']
