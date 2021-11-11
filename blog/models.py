from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Tags(models.Model):
    name = models.CharField(max_length=80)
    created_on = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return {self.name}

class SiteSettings(models.Model):
    title = models.CharField(max_length=200, unique=True)
    sub_title = models.CharField(max_length=100, unique=True)
    social_media_links = models.URLField(max_length=128, db_index=True, unique=True, blank=True)
