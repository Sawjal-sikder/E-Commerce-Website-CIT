# product/context_processors.py
from .models import Category, SubCategory

def categories_processor(request):
    categories = Category.objects.all()
    category_subcategory_map = {category: SubCategory.objects.filter(category=category) for category in categories}
    return {'category_subcategory_map': category_subcategory_map}
