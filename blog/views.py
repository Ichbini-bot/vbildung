from django.shortcuts import render
from .models import Post, Category
from django.http import HttpResponse
# from django.views.generic import ListView

# Create your views here.

def index(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    context = {
        'categories':categories,
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)

def page(request, category_id):
    categories = Category.objects.all()
    posts = Post.objects.filter(category_id=category_id)
    context = {
        'categories':categories,
        'posts': posts,
    }
    return render(request, 'blog/page.html', context)

def subpage(request, link):
    link_content = Post.objects.filter(link=link)
    categories = Category.objects.all()
    context = {
        'link_content':link_content,
        'categories':categories,
    }
    return render(request, 'blog/subpage.html', context)

