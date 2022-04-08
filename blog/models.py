from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Post(models.Model):

    # attributes:
    options = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    link = models.CharField(max_length=25, default='specify link')
    author = models.ForeignKey (User, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=10, choices=options, default='draft')
    publish = models.DateTimeField(default=timezone.now)


    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title