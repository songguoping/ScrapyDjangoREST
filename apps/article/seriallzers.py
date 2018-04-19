# -*- coding: utf-8 -*-
# @Time    : 17/4/18 11:31
__author__ = 'guoping'
from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
