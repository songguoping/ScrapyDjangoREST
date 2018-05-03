#!/usr/bin/env python
# encoding: utf-8

import xadmin
from .models import Article, ArticleTag


class ArticleAdmin(object):
    list_display = ["title", "url", "tags", "front_image_url", "front_image_path",
                    "comment_nums", "praise_nums", "fav_nums", "create_date", "crawl_time"]


class ArticleTagAdmin(object):
    list_display = ["name", "tag_type", "parent_tag", "add_time"]
    list_filter = ["tag_type", "parent_tag", "name"]
    search_fields = ['name', ]


xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(ArticleTag, ArticleTagAdmin)
