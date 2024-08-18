from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart, name='cart'),
    path('addtocart/<int:id>/', views.addToCart, name='addToCart'),
    path('remove/<int:id>/', views.cart_remove, name='cart_remove'),
    path('clear/cart/', views.clear_cart, name='clear_cart'),
    path('sscommerz/', views.sscommerz, name='sscommerz'),
    path('sscommerz/success/', views.success, name='success'),
    path('sscommerz/fail/', views.fail, name='fail'),
    path('sscommerz-cancel/', views.cancel, name='cancel'),
    path('coupon/', views.apply_coupon, name='apply_coupon'),
    path('wishlist/', views.wish_list, name='wishlist'),
    path('wish_remove/<int:id>', views.wish_remove, name='wish_remove'),
    path('add_wish/<int:id>', views.add_wish, name='add_wish'),

]

