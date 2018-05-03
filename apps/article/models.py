from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='标题')
    url = models.CharField(max_length=100, verbose_name='链接')
    url_object_id = models.CharField(max_length=50, verbose_name='链接md5值')
    tags = models.CharField(max_length=20, verbose_name='标签')
    content = UEditorField(verbose_name='内容', default='', null=True)
    front_image_url = models.CharField(max_length=300, null=True, verbose_name='封面图片链接')
    front_image_path = models.ImageField(upload_to='article/images/full', null=True, blank=True, verbose_name='封面图')
    comment_nums = models.IntegerField(default=0, verbose_name='评论数')
    praise_nums = models.IntegerField(default=0, verbose_name='点赞数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏数')

    create_date = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    crawl_time = models.DateTimeField(default=datetime.now, verbose_name='爬取时间')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ArticleTag(models.Model):
    """
    文章tag
    """
    TAG_TYPE = (
        (1, "一级标签"),
        (2, "二级标签"),
    )

    name = models.CharField(default="", max_length=30, verbose_name="标签名", help_text="标签名")
    url = models.CharField(default="", max_length=30, verbose_name="标签url", help_text="标签url")
    desc = models.TextField(default="",null=True, verbose_name="标签描述", help_text="标签描述")
    tag_type = models.IntegerField(choices=TAG_TYPE, verbose_name="标签级别", help_text="标签级别")
    parent_tag = models.ForeignKey("self", null=True, on_delete=models.CASCADE, blank=True, verbose_name="父标签级别",
                                   help_text="父标签",
                                   related_name="sub_tag")
    add_time = models.DateTimeField(default=datetime.now,null=True, verbose_name="添加时间")
    crawl_time = models.DateTimeField(null=True, verbose_name='爬取时间')

    class Meta:
        verbose_name = "商品标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
