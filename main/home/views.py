from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import slider,condation,offer
from products.models import Product, SubCategory, Brand

# Create your views here.
def contact_us(request):
    return render(request, 'contact.html',{})
@login_required(login_url='user_registration')

def home(request):
    all_slider = slider.objects.all()
    condations = condation.objects.all()
    Featureds = Product.objects.filter(is_Featured=True)
    Populars = Product.objects.filter(is_Popular=True)
    New_addeds = Product.objects.filter(is_New_added=True)
    SubCategorys = SubCategory.objects.all()
    offers = offer.objects.all()[:3]
    new_arrivals = Product.objects.all().order_by('-created')[:10]
    Brands = Brand.objects.all()[:10]
    return render(request, 'home.html',
                  {
                      'sliders':all_slider,
                      'condations':condations,
                      'Featureds':Featureds,
                      'Populars':Populars,
                      'New_addeds':New_addeds,
                      'SubCategorys':SubCategorys,
                      'offers':offers,
                      'new_arrivals':new_arrivals,
                      'Brands':Brands,
                  })