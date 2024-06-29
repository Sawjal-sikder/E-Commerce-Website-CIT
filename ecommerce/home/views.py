from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.models import Category, SubCategory, Product
from .models import Slider

# Create your views here.
@login_required(login_url='user_login')
def home(request):
    categories = Category.objects.all()
    category_subcategory_map = {category: SubCategory.objects.filter(category=category) for category in categories}
    sliders = Slider.objects.all()
    is_Featured = Product.objects.filter(is_Featured=True)
    is_Popular = Product.objects.filter(is_Popular=True)
    is_New_added = Product.objects.filter(is_New_added=True)
    New_Arrivals = Product.objects.all().order_by('-name')
    return render(request, 'home.html', 
    {
        'category_subcategory_map': category_subcategory_map,
        'sliders' : sliders,
        'is_Featured':is_Featured,
        'is_Popular':is_Popular,
        'is_New_added':is_New_added,
        'popular_catagory' : SubCategory.objects.all(),
        'New_Arrivals':New_Arrivals
    })
