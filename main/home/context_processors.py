from django.shortcuts import render
from products.models import Category, SubCategory, Product
from cart.models import Cart


def context_categories(request):
    user = request.user
    categories = {}
    carts = []
    cart_len = 0
    total = 0

    # Fetch categories and subcategories
    categors = Category.objects.all().prefetch_related('subcategories')
    for category in categors:
        subcategories = category.subcategories.all()
        categories[category] = subcategories

    # Cart context processors
    if user.is_authenticated:
        carts = Cart.objects.filter(user=user).select_related('product')
        cart_len = carts.count()
        for a in carts:
            total += a.product.new_price * a.qty

    return {
        'categories': categories,
        'carts': carts,
        'cart_len': cart_len,
        'total': total,
    }
