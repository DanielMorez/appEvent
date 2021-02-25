from rest_framework import viewsets, permissions, generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import PostSerializer
from .models import Post
from .utils import PostFilter


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    filterset_class = PostFilter
    ordering_fields = '__all__'
    http_method_names = ['get']
