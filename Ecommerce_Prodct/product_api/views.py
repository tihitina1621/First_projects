from django.shortcuts import render
#from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product, Category
from .serializer import ProductSerializer, CategorySerializer

#def index(request):
 #   return HttpResponse('Hey, Welcome to my very first thing')
class ProductViewSet(viewsets.ModelViewSet):   #the viewset enables to perform full CRUD functionality
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
