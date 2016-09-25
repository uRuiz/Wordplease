from django.contrib import admin

from categories.models import Category
from posts.models import Post


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_filter = ('categories',)

admin.site.register(Post, CategoryAdmin)
