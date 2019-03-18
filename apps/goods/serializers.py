#!/usr/bin/python
# -*- coding:utf-8 -*-
from rest_framework import serializers

from .models import GoodInfo, Good


class GoodInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodInfo
        fields = ('goods', 'brands',)


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = '__all__'

    def create(self, validated_data):
        return Good.objects.create(**validated_data)
