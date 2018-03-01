import json
from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Product, Address, Order, ShoppingCart, ShoppingCartDetails, Payment, User
from .serializable import  AddressSerializer, ProductsSerializer, ProductSerializer, ShoppingCartSerializer, TagSerializer
from rest_framework.permissions import AllowAny
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

# Create your views here.

class AddressView(APIView): #DONE
    #GET
    def get(self, request, user_id):
        address = Address.objects.all().filter(user = user_id)
        serializer = AddressSerializer(address, many=True)
        return Response(serializer.data)
    #PUT
    def put(self, request, user_id):
        
        # I get the content from the body request and convert it into a dictionary
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        the_user = User.objects.get(id = user_id)
        
        newAddress = Address(user = the_user,
        street_name = body['street_name'],
        city = body['city'],
        state = body['state'],
        country = body['country'],
        zipcode = body['zipcode'],
        phone_number = body['phone_number'])
        newAddress.save()
        
        serializer = AddressSerializer(newAddress, many=False)
        return Response(serializer.data)
    #DELETE
    def delete(self, request, user_id):
        
        the_user = User.objects.get(id = user_id)
        
        address = Address.objects.all().filter(user=the_user)
        address.delete()
        
        return Response("ok")
    
class AddressView_User(APIView): #DONE
    #GET
    def get(self, request, user_id, address_id):
        address = Address.objects.all().filter(user = user_id, id = address_id)
        serializer = AddressSerializer(address, many=True)
        return Response(serializer.data)
    #POST hacer una vista para un una direccion en especifica
    def post(self, request, user_id, address_id):
        # I get the content from the body request and convert it into a dictionary
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        the_user = User.objects.get(id = user_id)
        
        # Look for the game in the database and update the properties 
        # based on what came from the request
        address = Address.objects.get(pk= address_id)
        address = Address.objects.get(user = the_user)
        address.street_name = body['street_name']
        address.city = body['city']
        address.state = body['state']
        address.country = body['country']
        address.zipcode = body['zipcode']
        address.phone_number = body['phone_number']
        address.save()
        # serialize the response object and pass it back
        serializer = AddressSerializer(address, many=False)
        return Response(serializer.data)
    #DELETE
    def delete(self, request, user_id, address_id):
        
        the_user = User.objects.get(id = user_id)
        
        address = Address.objects.get(user=the_user, id = address_id)
        address.delete()
        
        return Response("ok")
    
class TagView(APIView):
    def get(self, request):
        tag = Product.objects.all()
        serializer = TagSerializer(tag, many=True)
        return Response(serializer.data)
        
class ProductsView(APIView): 
    #GET
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
        