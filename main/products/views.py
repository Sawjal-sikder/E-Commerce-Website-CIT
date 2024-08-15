from django.shortcuts import render
from .models import Product,SubCategory
# Create your views here.
def products(requests):
    pass



def single_product(requests, slug):
    one_product = Product.objects.get(slug=slug)
    subcategories = SubCategory.objects.filter(category=one_product.category)
    all_products = Product.objects.filter(category=one_product.category)
    return render(requests, 'single_product.html',
                  {
                      'one_product':one_product,
                      'subcategories':subcategories,
                      'all_products':all_products,
                  })