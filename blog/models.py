import re
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


def unescape_gist_embeds(escaped):
    regex = ("&lt;script src=(\"https:\\/\\/gist\\.github\\.com"
             "\\/johnpooch\\/[^\"]*\")&gt;&lt;\\/script&gt;")
    pattern = re.compile(regex, re.S)
    # replace all escaped gist scripts with non-escaped scripts
    return re.sub(pattern, r'<script src=\1></script>', escaped)


def substitute_code_snippets(text):
    regex = '`([^`]*)`'
    pattern = re.compile(regex, re.S)
    # replace all back-tick code snippets with span
    return re.sub(
        pattern,
        r'<span class="inline-code-snippet">\1</span>',
        text)


STATUS = ((0, "Draft"), (1, "Published"))


class Tag(models.Model):
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return str(self.name)


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

    @property
    def parsed_content(self):
        parsed = unescape_gist_embeds(self.content)
        parsed = substitute_code_snippets(parsed)
        return parsed

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


DEFAULT_CREATED_BY_ID = 1


class Comment(models.Model):
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField(blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE,
        default=DEFAULT_CREATED_BY_ID)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class SiteSettings(models.Model):
    title = models.CharField(max_length=200, unique=True)
    sub_title = models.CharField(max_length=100, unique=True)
    linkedin = models.URLField(
        max_length=128,
        db_index=True,
        unique=True,
        blank=True)
    github = models.URLField(
        max_length=128,
        db_index=True,
        unique=True,
        blank=True)
