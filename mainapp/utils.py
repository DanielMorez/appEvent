from django_filters.rest_framework import FilterSet, DateFromToRangeFilter

from .models import Post


class PostFilter(FilterSet):
    created = DateFromToRangeFilter()  # Используемые поля created_before, created_after
    # Пример, https:/127.0.0.1/posts/?created_before=02-02-2020?created_after=09-09-2021

    class Meta:
        model = Post
        fields = ('id', 'post_id', 'created')
