from rest_framework import serializers
from .models import Product, Address


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name_product','name_brand')
        
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('user_id','street_name_1','city')