from django.contrib import admin
from .models import Cart, Order, Coupon
# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'qty',]
admin.site.register(Cart,CartAdmin)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'qty','total_price', 'transaction_id','status']
admin.site.register(Order,OrderAdmin)

class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', ]
admin.site.register(Coupon,CouponAdmin)

