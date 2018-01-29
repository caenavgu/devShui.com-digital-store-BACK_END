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
    def get(self, request, product_id):
        product = Product.objects.get(pk=product_id)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)
    
    def put(self, request):
        
        # I get the content from the body request and convert it into a dictionary
        body_unicode = request.body.decode('utf-8')
        jsonObject = json.loads(body_unicode)
        
        newProduct = Product(name_product=jsonObject['name_product'],name_brand=jsonObject['name_brand'],description_product=jsonObject['description_product'],quantity=jsonObject['quantity'],)
        newGame.save()
        
        serializer = GameSerializer(newGame, many=False)
        return Response(serializer.data)