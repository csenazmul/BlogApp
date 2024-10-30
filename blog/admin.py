from django.contrib import admin

# Register your models here.

from blog import models as blog_models

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'status')
    search_fields = ('title', 'body')

admin.site.register(blog_models.Post, PostAdmin)

# from .models import Post

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'created_at')
#     search_fields = ('title', 'content')

# admin.site.register(Post)

