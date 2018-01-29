from django.contrib import admin
from .models import Product, Address, Orders 

# Register your models here.
admin.site.register(Product)
admin.site.register(Address)
admin.site.register(Orders)