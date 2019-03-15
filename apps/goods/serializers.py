#!/usr/bin/python
# -*- coding:utf-8 -*-
from rest_framework import serializers

from .models import GoodInfo


class GoodInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodInfo
        fields = ('goods', 'brands',)
