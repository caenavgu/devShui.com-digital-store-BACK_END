from django.shortcuts import render
import json
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Product, Address, Order, ShoppingCart
from .serializable import  AddressSerializer, OrderSerializer, ProductsSerializer, ProductSerializer

# Create your views here.

class AddressView(APIView):
    def get(self, request, user_id):
        address = Address.objects.all().filter(user_id = user_id)
        serializer = AddressSerializer(address, many=True)
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
    
class OrderView(APIView):
    def get(self, request, user_id):
        order = Order.objects.all().filter(user_id = user_id)
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)
        
def transactions(request, user_id):
    return HttpResponse("<h1>Here are the transactions for the user " + user_id + ".</h1>")