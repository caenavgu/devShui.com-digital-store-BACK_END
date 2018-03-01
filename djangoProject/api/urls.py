"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('user/<int:user_id>/address/', views.AddressView.as_view()), #DONE: GET - PUT -DELETE 
    path('user/<int:user_id>/address/<int:address_id>/', views.AddressView_User.as_view()), #DONE: GET - PUT -DELETE 
    path('tags/', views.TagView.as_view()), #DONE - Show all Tags
    path('products/', views.ProductsView.as_view()),  #DONE - Show all Products
    path('product/<str:product_id>/', views.ProductView.as_view()), #DONE - Show a particular product
<<<<<<< HEAD
    path('user/<int:user_id>/shoppingcart/<int:shoppingcart_id>/', views.ShoppingCartView_User.as_view()), #DONE - Show user's shopping cart
    
    
    

=======
    path('user/<int:user_id>/shoppingcart/<int:shoppingcart_id>/', views.ShoppingCartView_User.as_view()), #DONE - Show user's shopping cart 
>>>>>>> a85d1de6320f3069c124fee505a11443e683a766
]
