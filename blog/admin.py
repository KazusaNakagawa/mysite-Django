from django.contrib import admin

from blog.models import Category, Post, Tag

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
