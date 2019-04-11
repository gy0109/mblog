from django.db import models
from django.utils import timezone


# Create your models here.


class Post(models.Model):
    """存储文章的数据表"""
    title = models.CharField(max_length=30)   # 标题
    slug = models.SlugField(max_length=30)    # 网址
    abstract = models.CharField(max_length=50)
    body = models.TextField()                 # 文章内容
    pub_date = models.DateTimeField(default=timezone.now)   # 文章发表时间

    class Meta:
        ordering = ('-pub_date', )    # 按照什么排序  可多种

    # def __unicode__(self):
    #     return self.title             # 使用unicode 使标题可以正确的支持中文标题  可读性

    def __str__(self):
        return self.title


class NewTable(models.Model):
    # 常用数据类型的model
    bigint_f = models.BigIntegerField()
    bool_f = models.BooleanField()
    date_f = models.DateField(auto_now=True)     # 自动加入当前时间
    char_f = models.CharField(max_length=100)
    datatime_f = models.DateTimeField(auto_now_add=True)  # 对象被创建时才加入当前时间
    decimal_f = models.DecimalField(max_digits=10, decimal_places=2)   # 可接受最大位数  在所有位数中小数占几位
    float_f = models.FloatField(null=True)
    int_f = models.IntegerField(default=2010)
    text_f = models.TextField()

    # class Meta:
    #     ordering = ('int-f',)

    def __str__(self):
        return self.char_f


class Product(models.Model):
    sizes = (
        ('s', 'small'),
        ('M', 'medium'),
        ('L', 'Large')
    )
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=1, choices=sizes)

    class Meta:
        ordering = ['sku', ]

    def __str__(self):
        return self.name


class Phone(models.Model):
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    reper = models.IntegerField(default=0)

    class Meta:
        ordering = ['sku', ]
        # db_table = 'tb_heros'
        verbose_name = '中古手机'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

