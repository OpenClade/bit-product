from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response

from main.models import Product
from api.serializers import ProductCreateSerializer

import asyncio

class ProductList(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer

    
    
    

