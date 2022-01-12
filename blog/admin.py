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

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
