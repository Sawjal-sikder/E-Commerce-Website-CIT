from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, Order, Coupon
from sslcommerz_lib import SSLCOMMERZ
from home.context_processors import context_categories
from products.models import Product
import datetime
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import logging

# Create your views here.
def cart(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    return render(request, 'cart.html', {'cart_items': cart_items})

def addToCart(request, id):
    user = request.user
    product = Product.objects.get(id=id)
    cart_item, created = Cart.objects.get_or_create(user=user, product=product)
    if not created:
        # If it already exists, increase the quantity
        cart_item.qty += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER', '/'))


def cart_remove(request, id):
    cart_item = Cart.objects.get(id=id)
    cart_item.delete()
    return redirect('cart')


logger = logging.getLogger(__name__)
def sscommerz(request):
    user = request.user
    context = context_categories(request)
    total = context.get('total', 0)

    if total == 0:
        return redirect('cart')  # Redirect to cart if total is 0 or no items are in the cart

    settings = {'store_id': 'monim66a8f9b4d0919', 'store_pass': 'monim66a8f9b4d0919@ssl', 'issandbox': True}
    sslcommez = SSLCOMMERZ(settings)

    # Generate a unique transaction ID
    transaction_id = str(user.id) + str(int(datetime.datetime.now().timestamp()))

    # Create order
    for cart_item in Cart.objects.filter(user=user):
        order = Order.objects.create(
            user=user,
            product=cart_item.product,
            qty=cart_item.qty,
            total_price=cart_item.product.new_price * cart_item.qty,
            transaction_id=transaction_id
        )

    post_body = {}
    post_body['total_amount'] = total
    post_body['currency'] = "BDT"
    post_body['tran_id'] = transaction_id
    post_body['success_url'] = "http://127.0.0.1:8000/cart/sscommerz-success/"
    post_body['fail_url'] = "http://127.0.0.1:8000/cart/sscommerz-fail/"
    post_body['cancel_url'] = "http://127.0.0.1:8000/cart/sscommerz-cancel/"
    post_body['emi_option'] = 0
    post_body['cus_name'] = user.username
    post_body['cus_email'] = user.email
    post_body['cus_phone'] = "01700000000"  # You might want to store and use the user's actual phone number
    post_body['cus_add1'] = "customer address"  # Ideally fetch from user's profile
    post_body['cus_city'] = "Dhaka"
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = Cart.objects.filter(user=user).count()
    post_body['product_name'] = "Cart Items"
    post_body['product_category'] = "General"
    post_body['product_profile'] = "general"

    response = sslcommez.createSession(post_body)
    return redirect(response['GatewayPageURL'])

@csrf_exempt
def success(request):
    transaction_id = request.GET.get('tran_id')
    val_id = request.GET.get('val_id')
    bank_tran_id = request.GET.get('bank_tran_id')

    # Update order status to 'Complete'
    Order.objects.filter(transaction_id=transaction_id).update(status='Complete')

    # Clear the cart after successful payment
    cart = Cart.objects.filter(user=request.user)
    for i in cart:
        i.delete()


    return render(request, 'success.html', {'transaction_id': transaction_id})

@csrf_exempt
def fail(request):
    transaction_id = request.GET.get('tran_id')

    # Update order status to 'Failed'
    Order.objects.filter(transaction_id=transaction_id).update(status='Failed')

    return render(request, 'fail.html', {'transaction_id': transaction_id})

@csrf_exempt
def cancel(request):
    transaction_id = request.GET.get('tran_id')

    # Update order status to 'Canceled'
    Order.objects.filter(transaction_id=transaction_id).update(status='Canceled')

    return render(request, 'cancel.html', {'transaction_id': transaction_id})

def clear_cart(request):
    if request.user.is_authenticated:
        Cart.objects.filter(user=request.user).delete()
    return redirect('cart')


def apply_coupon(request):
    if request.method == 'POST':
        code = request.POST.get('Coupon')
        try:
            coupon = Coupon.objects.get(code=code)
        except Coupon.DoesNotExist:
            messages.error(request, 'Invalid coupon code')
            return redirect('cart')

        if not coupon.is_valid():
            messages.error(request, 'This coupon has expired or is inactive')
            return redirect('cart')

        cart = Cart.objects.get(user=request.user)
        if cart.total < coupon.min_purchase:
            messages.error(request, f'Cart total must be at least {coupon.min_purchase} to use this coupon')
            return redirect('cart')

        if coupon.discount_type == 'percent':
            discount_amount = (coupon.discount / 100) * cart.total
        else:
            discount_amount = coupon.discount

        cart.total -= discount_amount
        cart.save()

        messages.success(request, f'Coupon applied! You saved {discount_amount}')
        return redirect('cart')

    return redirect('cart')


