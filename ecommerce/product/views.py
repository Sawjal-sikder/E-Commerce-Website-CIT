from django.shortcuts import render
from .models import Product, SubCategory
from django.db.models import Q
# Create your views here.

def categories(request, slug):
    catagories_products = Product.objects.filter(sub_category__slug=slug)
    return render(request, 'category_products.html',{'catagories_products':catagories_products})
def product(request):
    products = Product.objects.all()
    return render(request, 'products.html',{'products':products})

def single_product(request, slug):
    single_product = Product.objects.get(slug=slug)
    subcategories = single_product.sub_category.category.subcategories.all()
    related_products = single_product.sub_category.products.exclude(id=single_product.id)
    return render(request,'single_product.html',
                  {
                      'single_product':single_product,
                      'subcategories':subcategories,
                      'related_products':related_products,

                  })



def serarch(request):
    if request.method == 'GET':
        query_search = request.GET.get('search')
        print(query_search)
        if query_search:
            products = Product.objects.filter(name__icontains=query_search)
    return render(request, 'products.html',
                  {
                      'products':products
                  })

