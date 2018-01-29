from django.shortcuts import render
import json
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Product
from .serializable import ProductSerializer

# Create your views here.

def transactions(request, user_id):
    return HttpResponse("<h1>Here are the transactions for the user " + user_id + ".</h1>")
    
class ProductsView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
        
class Address(APIView):
    def get(self, request):
        address = Address.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
        
