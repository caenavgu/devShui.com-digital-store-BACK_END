from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Address(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    street_name = models.CharField(max_length=30, default = '')
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipcode = models.PositiveIntegerField()    
    phone_number = models.PositiveIntegerField()

    def __int__(self):
        return self.zipcode

    class Meta:
        ordering = ('user_id', 'street_name', 'state', 'city', 'zipcode', 'phone_number',)
        
class Product(models.Model):
    name_product = models.CharField(max_length=30)
    name_brand = models.CharField(max_length=30)
    product_status = models.CharField(max_length=30)
    description_product = models.CharField(max_length=140)
    price_product = models.DecimalField(max_digits=5, decimal_places=2)
    quantity_products_stock = models.PositiveIntegerField(default=0)
    product_tag = models.CharField(max_length=30, default = '')
    
    def __str__(self):
        return self.name_product

    class Meta:
        ordering = ('name_product', 'name_brand', 'price_product','quantity_products_stock',)

class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=30)
    products = models.ManyToManyField(Product, through='ShoppingCart')

    def __str__(self):
        return self.order_status

    class Meta:
        ordering = ('id', 'user_id','order_status')
        
class ShoppingCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name_product = models.CharField(max_length=30)
    quantity_products = models.PositiveIntegerField(default=0)
    total_price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.order_status

    class Meta:
        ordering = ('id', 'name_product', 'quantity_products')
        
class Payment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    name_card = models.CharField(max_length=25)
    number_card = models.PositiveIntegerField(default=0)
    expiration_date = models.DateField(null=True)

    def __int__(self):
        return self.number_card

    class Meta:
        ordering = ('id', 'name_card', 'number_card', 'expiration_date',)
        
class Transaction(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    card_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    transaction_date = models.DateField(null=True)
    items_price = models.PositiveIntegerField(default=0)
    shipping_price = models.PositiveIntegerField(default=0)
    total_before_tax = models.PositiveIntegerField(default=0)
    estimated_tax = models.PositiveIntegerField(default=0)
    order_total = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.transaction_date

    class Meta:
        ordering = ('id', 'transaction_date', 'order_total', )
        