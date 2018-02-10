from django.contrib import admin
from .models import Product, Address, Order, ShoppingCart, Payment,  Tag, ShoppingCartDetails

# Register your models here.
admin.site.register(Address)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(ShoppingCart)
admin.site.register(ShoppingCartDetails)
admin.site.register(Payment)