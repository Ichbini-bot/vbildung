from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('<str:crypto>/', views.crypto, name='crypto'),
    #path('<int:pk>/', views.post_single, name='post_single'),
]