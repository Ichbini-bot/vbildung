from django.shortcuts import render
from .models import Post, Category
from django.http import HttpResponse
# from django.views.generic import ListView

# Create your views here.

def navbartop(request):
    categories = Category.objects.all()
    context = {
        'categories':categories,
    }
    return render(request, 'blog/navbartop.html', context)

def navbarleft(request, category_id):
    links = Post.objects.filter(category_id=category_id)
    context = {
        'links':links,
    }
    return render(request, 'blog/navbarleft.html', context)

def content(request, link):
    link_content = Post.objects.filter(link=link)
    context = {
        'link_content':link_content,
    }
    return render(request, 'blog/content.html', context)
