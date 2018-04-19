#!/usr/bin/env python
# encoding: utf-8

import xadmin
from .models import Article


class GoodsAdmin(object):
    list_display = ["title", "url", "tags", "front_image_url", "front_image_path",
                    "comment_nums", "praise_nums", "fav_nums", "create_date", "crawl_time"]



xadmin.site.register(Article, GoodsAdmin)


