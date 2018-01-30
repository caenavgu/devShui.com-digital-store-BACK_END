from django.shortcuts import render
import json
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Product, Address
from .serializable import ProductSerializer, AddressSerializer


# Create your views here.

def transactions(request, user_id):
    return HttpResponse("<h1>Here are the transactions for the user " + user_id + ".</h1>")
    
class ProductsView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
        
class AddressView(APIView):
    def get(self, request, user_id):
        address = Address.objects.all().filter(user_id = user_id)
        serializer = AddressSerializer(address, many=True)
        return Response(serializer.data)
        
