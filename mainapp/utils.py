from django_filters.rest_framework import FilterSet, DateFromToRangeFilter

from .models import Post


class PostFilter(FilterSet):
    created = DateFromToRangeFilter()

    class Meta:
        model = Post
        fields = ('id', 'post_id', 'created')
