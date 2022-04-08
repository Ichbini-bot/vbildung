from django.shortcuts import render
from .models import Post, Category
# from django.views.generic import ListView

# Create your views here.

def home(request):
    all_posts = Post.objects.all().filter(status='published')
    all_categories = Category.objects.all()
    context = {
        'posts': all_posts,
        'categories': all_categories,
        }
    return render(request, 'base.html', context)

'''
def post_single(request, pk):
    post = Post.objects.get(pk=pk, status='published')
    context = {'post': post}
    return render(request, 'index.html', {'post': post})
'''
import pdb

def crypto(request, crypto):
    pdb.set_trace()
    post = Post.objects.select_related('crypto')
    context = {'post': crypto}
    return render(request, 'index.html', context)
    
