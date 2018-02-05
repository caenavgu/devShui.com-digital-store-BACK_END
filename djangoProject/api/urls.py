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
    # GET
    path('user/<int:user_id>/address', views.AddressView.as_view()),
    path('products/', views.ProductsView.as_view()),  #show all products
    path('product/<str:product_id>', views.ProductView.as_view()), #show a particular product
    
    
    
    # path('products/<str:tags>', views.ProductsView.as_view()),
    path('user/<str:user_id>/order', views.transactions),
    path('user/<user_id>/order/<str:status>', views.transactions),
    # path('user/<int:user_id>/transactions', views.TransactionsView.as_view()),

]
