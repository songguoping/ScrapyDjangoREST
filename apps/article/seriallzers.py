# -*- coding: utf-8 -*-
# @Time    : 17/4/18 11:31
__author__ = 'guoping'
from rest_framework import serializers
from .models import Article, ArticleTag


class TagSerializer2(serializers.ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    sub_tag = TagSerializer2(many=True)

    class Meta:
        model = ArticleTag
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    category = TagSerializer()

    class Meta:
        model = Article
        fields = "__all__"
