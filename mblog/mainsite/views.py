from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime

from django.template.loader import get_template

from .models import Post
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
        if posts != None:
            html = template.render(locals())
            return HttpResponse(html)

    except:
        return redirect('/homepagetem/')        # 回首页





