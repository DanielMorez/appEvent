from django.http import HttpResponse
from rest_framework import viewsets, permissions, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.views.generic import TemplateView

from .serializers import PostSerializer
from .models import Post
from .utils import PostFilter
from .tasks import update_news


def get_update(request):
    """ Вызов проверки обновлений по-требованию """
    update_news.delay()
    return HttpResponse('Успешно!')


class GetUpdateView(TemplateView):
    """ Кнопка для вызова """
    template_name = 'base.html'


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """ Отображение доступных методов API """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    filterset_class = PostFilter
    ordering_fields = '__all__'
    http_method_names = ['get']
