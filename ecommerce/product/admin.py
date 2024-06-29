from django.contrib import admin
from .models import Category, SubCategory, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'slug', 'tag')
    search_fields = ('name', 'slug', 'tag')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'sub_category', 'sku', 'stock', 'updated', 'slug')
    search_fields = ('name', 'sku', 'slug')
    list_filter = ('category', 'sub_category')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
