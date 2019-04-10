from django.db import models
from django.utils import timezone


# Create your models here.


class Post(models.Model):
    """存储文章的数据表"""
    title = models.CharField(max_length=30)   # 标题
    slug = models.CharField(max_length=30)    # 网址
    body = models.TextField()                 # 文章内容
    pub_date = models.DateTimeField(default=timezone.now)   # 文章发表时间

    class Meta:
        ordering = ('-pub_date', )    # 按照什么排序  可多种

    # def __unicode__(self):
    #     return self.title             # 使用unicode 使标题可以正确的支持中文标题  可读性

    def __str__(self):
        return self.title