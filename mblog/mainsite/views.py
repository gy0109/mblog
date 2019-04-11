import random

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from datetime import datetime
from django.template.loader import get_template

from .models import Post, Phone
# Create your views here.


def homepage(request):
    """获取所有文章 并通过django传递到客户端"""
    posts = Post.objects.all()
    post_lists = []
    for count, post in enumerate(posts):
        post_lists.append('No: {}'. format(str(count)) + str(post) + '<br>')
        post_lists.append('<small>' + str(post.body) + '</small><br><br>')
    return HttpResponse(post_lists)


# homepagetem
def homepage_tem(request):
    """获取所有文章 并通过django传递到客户端"""
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()                # 模板设置其他回复 若忘记传  有其他进行代替
    html = template.render(locals())
    return HttpResponse(html)


# post/(\w+)
def show_post(request, slug):
    """获取所有文章 并通过django传递到客户端"""
    template = get_template('post.html')        # 获取模板  要提供模板所需字段
    now = datetime.now()                        # 模板设置其他回复 若忘记传  有其他进行代替
    try:
        posts = Post.objects.get(slug=slug)     # 获取slug字段的text
        if posts is not None:
            html = template.render(locals())
            return HttpResponse(html)
    except Exception:
        return redirect('/homepagetem/')        # 回首页


def about(request):
    template = get_template('about.html')
    return HttpResponse(template.render(locals()))


def about_tem(request):
    template = get_template('about_tem.html')
    quotes = ['今日事今日毕',
              '少壮不努力，老大徒伤悲',
              '知识就是力量',
              '一个人的知识可以改变命运']
    return HttpResponse(template.render({'quotes': random.choice(quotes)}))


def phone(request):
    template = get_template('phone.html')
    phones = Phone.objects.all()
    return HttpResponse(template.render(locals()))


def phone_sku(request, sku):

    try:
        p = Phone.objects.get(sku=sku)
    except Phone.DoesNotExist:
        raise Http404('找不到指定的编号')
    template = get_template('phone_sku.html')
    # return HttpResponse(template.render(locals()))
    return HttpResponse(template.render({'p': p}))


