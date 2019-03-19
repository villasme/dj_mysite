from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend

from .models import GoodInfo, Good
from .serializers import GoodInfoSerializer, GoodsSerializer
from .filters import GoodsFilter


class GoodInfoView(viewsets.ModelViewSet):
    queryset = GoodInfo.objects.all()
    serializer_class = GoodInfoSerializer


class GoodPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'pg'


class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_class = GoodsFilter
    search_fields = ('goodsName',)

