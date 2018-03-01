from rest_framework import serializers
from .models import Product, Address, Order, ShoppingCart, ShoppingCartDetails, Payment, Tag
        
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('user', 'id', 'street_name', 'state', 'city', 'zipcode', 'phone_number')
        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name_tag')

class ProductsSerializer(serializers.ModelSerializer):
    product_tag = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id','url_image_product','name_product', 'name_brand', 'description_product', 'product_tag',  'quantity_products_stock', 'price_product', 'product_status')

class ProductSerializer(serializers.ModelSerializer):
    product_tag = TagSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = ('id','name_product', 'name_brand', 'description_product', 'product_tag',  'quantity_products_stock', 'price_product', 'product_status')
        
class ShoppingCartDetailsSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = ShoppingCartDetails
        fields = ('id')
        
class ShoppingCartSerializer(serializers.ModelSerializer):
    products_cart = ProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = ShoppingCart
        fields = ('id', 'user_id', 'status_shopping_cart', 'products_cart',)