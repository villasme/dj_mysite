#!/usr/bin/python
# -*- coding:utf-8 -*-
import xadmin
from .models import Good, GoodBrand, GoodInfo


class GoodsAdmin(object):
    list_display = ['goodsName', 'goodsNum', 'goodsPrice', 'goodsSpecId']
    search_fields = ['goodsName']


class GoodBrandAdmin(object):
    list_display = ['name', 'desc', 'image']
    search_fields = ['name']


class GoodInfoAdmin(object):
    list_display = ['goods', 'brands']


xadmin.site.register(Good, GoodsAdmin)
xadmin.site.register(GoodBrand, GoodBrandAdmin)
xadmin.site.register(GoodInfo, GoodInfoAdmin)
