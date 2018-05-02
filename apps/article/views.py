from django.shortcuts import render
from rest_framework import mixins
from  rest_framework.response import Response
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .models import Article
from .seriallzers import ArticleSerializer


# Create your views here.
class ArticlePagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class ArticleListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet,
                         mixins.UpdateModelMixin):
    """
    文章列表页 分页 搜索 过滤 排序
    """

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticlePagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('praise_nums', 'create_date')

    def put(self, request, *args, **kwargs):

        return self.update(request, *args, **kwargs)
