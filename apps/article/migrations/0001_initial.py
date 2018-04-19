# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-19 10:38
from __future__ import unicode_literals

import DjangoUeditor.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('url', models.CharField(max_length=100, verbose_name='链接')),
                ('url_object_id', models.CharField(max_length=50, verbose_name='链接md5值')),
                ('tags', models.CharField(max_length=20, verbose_name='标签')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('front_image_url', models.CharField(max_length=300, null=True, verbose_name='封面图片链接')),
                ('front_image_path', models.ImageField(blank=True, null=True, upload_to='article/images/full', verbose_name='封面图')),
                ('comment_nums', models.IntegerField(default=0, verbose_name='评论数')),
                ('praise_nums', models.IntegerField(default=0, verbose_name='点赞数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏数')),
                ('create_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('crawl_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='爬取时间')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
    ]