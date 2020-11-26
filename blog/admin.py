from django.contrib import admin
from .models import (
    BlogCover,
    BlogCategory,
    BlogPost
)


@admin.register(BlogCover)
class BlogCoverAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp']


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'timestamp']


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_name', 'owner', 'timestamp']
