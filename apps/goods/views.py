from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination

from .models import GoodInfo, Good
from .serializers import GoodInfoSerializer, GoodsSerializer


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
