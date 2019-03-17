from django_filters import rest_framework as filters

from .models import Good


class GoodsFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='goodsPrice', lookup_expr='gte', help_text='最低价格')
    max_price = filters.NumberFilter(field_name='goodsPrice', lookup_expr='lte', help_text='最高价格')

    class Meta:
        model = Good
        fields = ('goodsName', 'goodsNum', 'goodsPrice', )
