from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    #path('', views.navbartop, name = 'navbartop'),
    path('', views.index, name = 'index'),
    path('<int:category_id>/', views.page, name = 'page'),
    path('<str:link>/', views.subpage, name = 'subpage'),
    #path('<int:category_id>/', views.navbarleft, name = 'navbarleft'),
    #path('<str:link>/', views.content, name = 'content'),
]
