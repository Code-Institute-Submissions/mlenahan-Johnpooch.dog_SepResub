import re
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


STATUS = ((0, "Draft"), (1, "Published"))

class Tag(models.Model):
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.name

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
    tags = models.ManyToManyField(Tag, blank=True)
    
    class Meta:
        ordering = ["created_at"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def parsed_content(self):
        # regex to find escaped gist scripts
        gist_script_regex = "&lt;script src=\"(https:\/\/gist\.github\.com\/johnpooch\/.*)\"&gt;&lt;\/script&gt;"
        pattern = re.compile(gist_script_regex, re.S)
        # replace all escaped gist scripts with non-escaped scripts
        subbed = re.sub(pattern, r'<script src=\1></script>', self.content)
        code_snippet_regex = '`(.*)`'
        pattern = re.compile(code_snippet_regex, re.S)
        # replace all back-tick code snippets with span
        subbed = re.sub(pattern, r'<span class="inline-code-snippet">\1</span>', subbed)
        return subbed


class SiteSettings(models.Model):
    title = models.CharField(max_length=200, unique=True)
    sub_title = models.CharField(max_length=100, unique=True)
    linkedin = models.URLField(max_length=128, db_index=True, unique=True, blank=True)
    github = models.URLField(max_length=128, db_index=True, unique=True, blank=True)
