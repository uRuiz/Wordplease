from django.contrib import admin
from categories.models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('category_name',)

admin.site.register(Category, CategoryAdmin)
