from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.


def homepage(request):
    """获取所有文章 并通过django传递到客户端"""
    posts = Post.objects.all()
    post_lists = []
    for count, post in enumerate(posts):
        post_lists.append('No: {}'. format(str(count)) + str(post) + '<br>')

    return HttpResponse(post_lists)