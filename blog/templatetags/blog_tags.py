#! C:\Python36\python.exe
# coding:utf-8
'''
about what
'''
from django import template
from blog.models import Post,Category

register = template.Library()

#定义最新文章的标签
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by("-create_time")[:num]

# 定义归档的标签


@register.simple_tag
def archives(num=5):
    return Post.objects.dates("create_time","month",order="DESC")

# 定义分分类的标签
@register.simple_tag
def get_categories():
    return Category.objects.all()