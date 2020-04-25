from django.contrib import admin

from blog.models import Category, ContentImage, Post, Tag


class ContentImageInline(admin.TabularInline):
    """ Use admin's "inline" feature to allow editing from the parent model page."""
    model = ContentImage
    extra = 1


class PostAdmin(admin.ModelAdmin):
    # Image in post
    inlines = [
        ContentImageInline,
    ]


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
