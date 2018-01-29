from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name_product = models.CharField(max_length=30)
    name_brand = models.CharField(max_length=30)
    description_product = models.CharField(max_length=140)
    quantity = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name_product

    class Meta:
        ordering = ('name_product',)
        
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_name_1 = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipcode = models.PositiveIntegerField()    
    phone_number = models.PositiveIntegerField()
    special_notes = models.CharField(max_length=300,default=None)

    
    def __str__(self):
        return self.zipcode

    class Meta:
        ordering = ('zipcode',)
        
class Orders(models.Model):
    headline = models.CharField(max_length=100)
    product = models.ForeignKey(Product, max_length=100, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity_buy = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)