from django.contrib import admin
from .models import Category, SubCategory, Brand, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'slug', 'tag')
    search_fields = ('name', 'description', 'tag')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'sub_category', 'sku', 'stock', 'updated', 'slug', 'brand', 'is_Featured', 'is_Popular', 'is_New_added')
    search_fields = ('name', 'description', 'sku')
    list_filter = ('category', 'sub_category', 'brand', 'is_Featured', 'is_Popular', 'is_New_added')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('updated',)

# Remember to replace 'brand' with 'Brand' in the models.py as model names should follow CamelCase
