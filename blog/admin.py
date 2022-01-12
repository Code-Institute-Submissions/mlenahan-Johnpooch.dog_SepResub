from django.contrib import admin
from .models import Tag, Post, SiteSettings, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_at')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_at')
    summernote_fields = ('content')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = ('name', 'created_at')
    search_fields = ['name']
    list_filter = ('name', 'created_at')


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):

    list_display = ('title', 'sub_title', 'linkedin', 'github')
    search_fields = ['title', 'sub_title', 'linkedin', 'github']
    list_filter = ('sub_title', 'linkedin', 'github')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('post', 'name', 'created_at')
    search_fields = ['post', 'name']
    list_filter = ('post', 'name', 'created_at')
