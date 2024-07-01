from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to='category_thumbnails/', blank=True, null=True)
    banner = models.ImageField(upload_to='category_banners/', blank=True, null=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    tag = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='subcategory_thumbnails/', blank=True, null=True)
    banner = models.ImageField(upload_to='subcategory_banners/', blank=True, null=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='brand_thumbnails/')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()
    sku = models.CharField(max_length=100, unique=True)
    stock = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    image1 = models.ImageField(upload_to='product_images/')
    image2 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    banner = models.ImageField(upload_to='product_banners/', blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brands', null=True, blank=True)
    is_Featured = models.BooleanField(default=False)
    is_Popular = models.BooleanField(default=False)
    is_New_added = models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
