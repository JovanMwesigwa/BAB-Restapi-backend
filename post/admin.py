from django.contrib import admin
from .models import Post, Comment, Category, LikePost


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ['name']}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', ]
    # prepopulated_fields	= {'slug':['title']}


admin.site.register(Comment)
admin.site.register(LikePost)
