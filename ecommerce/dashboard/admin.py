from django.contrib import admin
from .models import Address

class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'address1', 'address2', 'state', 'city', 'county')

admin.site.register(Address, AddressAdmin)
