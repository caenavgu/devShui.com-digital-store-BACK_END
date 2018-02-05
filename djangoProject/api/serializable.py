from rest_framework import serializers
from .models import Product, Address, Order, ShoppingCart
        
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('user_id','street_name_1','city', 'zipcode', 'id')

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name_product')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name_product','name_brand')
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user_id','name_product','name_brand')
        
class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'name_product','quantity_products')