import json
from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Product, Address, Order, ShoppingCart, ShoppingCartDetails, Payment
from .serializable import  AddressSerializer, ProductsSerializer, ProductSerializer, ShoppingCartSerializer, TagSerializer
from rest_framework.permissions import AllowAny
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

# Create your views here.

class AddressView(APIView): #DONE
    def get(self, request, user_id):
        address = Address.objects.all().filter(user_id = user_id)
        serializer = AddressSerializer(address, many=True)
        return Response(serializer.data)
    
class TagView(APIView):
    def get(self, request):
        tag = Product.objects.all()
        serializer = TagSerializer(tag, many=True)
        return Response(serializer.data)
        
class ProductsView(APIView): 
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)
        
class ProductView(APIView):
    def get(self, request, product_id):
        product = Product.objects.all().filter(id = product_id)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
        
class ShoppingCartView_User(APIView):
    def get(self, request, user_id, shoppingcart_id):
        shoppingcart = ShoppingCart.objects.all().filter(user_id = user_id).filter(id = shoppingcart_id)
        serializer = ShoppingCartSerializer(shoppingcart, many=True)
        return Response(serializer.data)
    
def transactions(request, user_id):
    return HttpResponse("<h1>Here are the transactions for the user " + user_id + ".</h1>")
    
class ImageView(APIView):
    def get(self, request, image_name):
        permission_classes = (AllowAny,)
        f = open('./static/'+image_name, 'rb')
        return HttpResponse(f,content_type='image/png')
        