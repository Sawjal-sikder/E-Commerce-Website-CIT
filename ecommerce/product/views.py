from django.shortcuts import render
from .models import Product
from django.db.models import Q
# Create your views here.
def product(request):
    products = Product.objects.all()
    return render(request, 'products.html',
                  {
                      'products':products
                  })

def single_product(request, slug):
    single_product = Product.objects.get(slug=slug)
    return render(request,'single_product.html',
                  {
                      'single_product':single_product
                  })
def serarch(request):
    if request.method == 'GET':
        query_search = request.GET.get('search')
        print(query_search)
        if query_search:
            products = Product.objects.filter(Q(name__icontains=query_search) | Q(sub_category__icontains=query_search))
    return render(request, 'products.html',
                  {
                      'products':products
                  })

