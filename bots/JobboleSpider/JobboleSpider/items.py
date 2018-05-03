# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import datetime
import re

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join
# from scrapy_djangoitem import DjangoItem
# from article.models import Article
from JobboleSpider.settings import SQL_DATETIME_FORMAT


def date_convert(value):
    try:
        create_date = datetime.datetime.strptime(value, "%Y/%m/%d").date()
    except Exception as e:
        create_date = datetime.datetime.now().date()

    return create_date


def return_value(value):
    return value


def get_nums(value):
    match_re = re.match(".*?(\d+).*", value)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0

    return nums


def remove_comment_tags(value):
    # 去掉tag中提取的评论
    if "评论" in value:
        return ""
    else:
        return value


class ArticleItemLoader(ItemLoader):
    # 自定义itemLoader
    default_output_processor = TakeFirst()


class JobBoleArticleItem(scrapy.Item):
    # django_model = Article
    title = scrapy.Field()
    create_date = scrapy.Field(
        # input_processor=MapCompose(date_convert)
    )
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field(
        output_processor=MapCompose(return_value)
    )
    front_image_path = scrapy.Field()
    praise_nums = scrapy.Field(
        # input_processor=MapCompose(get_nums)
    )
    comment_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    fav_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    tags = scrapy.Field(
        input_processor=MapCompose(remove_comment_tags),
        output_processor=Join(",")
    )
    content = scrapy.Field(
        output_processor=Join("")
    )
    crawl_time = scrapy.Field()

    def make_data_clean(self):
        front_image_url = ""
        # content = remove_tags(self["content"])
        self["crawl_time"] = datetime.datetime.now().strftime(SQL_DATETIME_FORMAT)
        if self["front_image_url"]:
            self["front_image_url"] = self["front_image_url"][0]
        str = self["create_date"].strip().replace("·", "").strip()
        self["create_date"] = datetime.datetime.strptime(
            str, "%Y/%m/%d").date()
        nums = 0
        value = self["praise_nums"]
        match_re = re.match(".*?(\d+).*", value)
        if match_re:
            nums = int(match_re.group(1))
        else:
            nums = 0
        self["praise_nums"] = nums

    def get_insert_sql(self):
        insert_sql = """
            insert into article_article(title, url, url_object_id,create_date, fav_nums, front_image_url, front_image_path,
            praise_nums, comment_nums, tags, content,crawl_time)
            VALUES (%s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s,%s) ON DUPLICATE KEY UPDATE fav_nums=VALUES(fav_nums),praise_nums=VALUES(praise_nums),comment_nums=VALUES(comment_nums),crawl_time=VALUES(crawl_time)
        """
        self.make_data_clean()
        params = (
            self["title"],
            self["url"],
            self["url_object_id"],
            self["create_date"],
            self["fav_nums"],
            self["front_image_url"],
            self["front_image_path"],
            self["praise_nums"],
            self["comment_nums"],
            self["tags"],
            self["content"],
            self["crawl_time"]
        )
        return insert_sql, params


class JobBoleArticleTagItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    tag_type = scrapy.Field()
    id = scrapy.Field()
    parent_tag_id = scrapy.Field()
    crawl_time = scrapy.Field()

    def make_data_clean(self):
        self["crawl_time"] = datetime.datetime.now().strftime(SQL_DATETIME_FORMAT)

    def get_insert_sql(self):
        insert_sql = """
               insert into article_articletag(name, url, tag_type,id, parent_tag_id,crawl_time)
               VALUES (%s, %s, %s,%s, %s, %s) ON DUPLICATE KEY UPDATE name=VALUES(name),url=VALUES(url),tag_type=VALUES(tag_type),crawl_time=VALUES(crawl_time),parent_tag_id=VALUES(parent_tag_id)
           """
        self.make_data_clean()
        params = (
            self["name"],
            self["url"],
            self["tag_type"],
            self["id"],
            self["parent_tag_id"],
            self["crawl_time"]
        )
        return insert_sql, params