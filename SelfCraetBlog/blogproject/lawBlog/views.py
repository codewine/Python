from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

# def index(request):
#     return HttpResponse("欢迎访问我的博客首页！")


# def index(request):
#     return render(request, 'lawBlog/index.html', context={
#                       'title': '我的博客首页',
#                       'welcome': '欢迎访问我的博客首页'
#                   })


from .models import Post
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'lawBlog/index.html', context={'post_list': post_list})



def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'lawBlog/detail.html', context={'post': post})