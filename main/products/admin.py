from django.contrib import admin
from .models import Category, SubCategory, Brand, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'slug',)
    search_fields = ('name', 'description', )
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'created','modified',)
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'sub_category', 'sku', 'stock',)
    search_fields = ('name', 'category', 'sub_category', 'sku', 'stock',)
    list_filter = ('name', 'category', 'sub_category', 'sku', 'stock',)
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('updated',)

# Remember to replace 'brand' with 'Brand' in the models.py as model names should follow CamelCase