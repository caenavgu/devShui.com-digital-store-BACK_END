from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Address(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    street_name = models.CharField(max_length=140, default = None)
    city = models.CharField(max_length=30, default = None)
    state = models.CharField(max_length=30, default = None)
    country = models.CharField(max_length=30, default = 'United State')
    zipcode = models.PositiveIntegerField(default = 00000)    
    phone_number = models.PositiveIntegerField( default = 0000000000)

    def __int__(self):
        return self.phone_number

    class Meta:
        ordering = ('user_id', 'id')
        
class Tag(models.Model):
    name_tag = models.CharField(max_length=30, default = None)
    descripcion_tag = models.CharField(max_length=300, default = None)
    
    def __str__(self):
        return self.name_tag

    class Meta:
        ordering = ('id', 'name_tag')
        
class Product(models.Model):
    PRODUCT_STATUS_CHOISE = (('AVAILABLE', 'available'), ('UNAVAILABLE', 'unavailable'))
    name_product = models.CharField(max_length=30)
    name_brand = models.CharField(max_length=30, default = None)
    product_status = models.CharField(max_length=30, choices = PRODUCT_STATUS_CHOISE,  default = 'available')
    description_product = models.CharField(max_length=300, default = None)
    price_product = models.DecimalField(max_digits=5, decimal_places=2)
    quantity_products_stock = models.PositiveIntegerField(default=0)
    product_tags = models.ManyToManyField(Tag, default = None)
    
    def __str__(self):
        return self.name_product

    class Meta:
        ordering = ('id', 'name_product', 'name_brand', 'product_status')

class ShoppingCart(models.Model):
    SHOPPING_CART_STATUS_CHOISE = (('EMPTY', 'empty'),('FULL', 'full'))
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status_shopping_cart = models.CharField(max_length=30, choices = SHOPPING_CART_STATUS_CHOISE, default='EMPTY')
    products_cart = models.ManyToManyField(Product, through='ShoppingCartDetails')

    def __str__(self):
        return self.order_status

    class Meta:
        ordering = ('id', 'user_id','status_shopping_cart')
        
class ShoppingCartDetails(models.Model):
    shopping_cart_id = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_product = models.PositiveIntegerField(default=0)
    total_price_product = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.order_status

    class Meta:
        ordering = ('id', 'product_id', 'quantity_product')
        
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
        
class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    shopping_cart_id = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    card_id = models.ForeignKey(Payment, on_delete=models.CASCADE, default = None)
    order_date = models.DateField(null=True)
    shipping_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    shipping_price = models.PositiveIntegerField(default=0)
    total_before_tax = models.PositiveIntegerField(default=0)
    estimated_tax = models.PositiveIntegerField(default=0)
    total_price = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.order_date

    class Meta:
        ordering = ('id', 'order_date', 'total_price', )
        