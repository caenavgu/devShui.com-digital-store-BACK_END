from django.contrib import admin
from .models import Product, Address, Order, ShoppingCart, Payment, Transaction

# Register your models here.
admin.site.register(Address)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(ShoppingCart)
admin.site.register(Payment)
admin.site.register(Transaction)