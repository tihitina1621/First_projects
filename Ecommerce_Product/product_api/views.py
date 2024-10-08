from django.shortcuts import render
from rest_framework import viewsets, generics, filters
#from .permissions import IsAuthorOrReadOnly
#from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product, Category
from .serializer import ProductSerializer, CategorySerializer
from .filters import ProductFilter

class CategoryViewSet(viewsets.ModelViewSet):   #the viewset enables to perform full CRUD functionality
    #authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
class ProductViewSet(viewsets.ModelViewSet):
    #authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]  #filters a product name and support partial matches
    filterset_class = ProductFilter
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer     #filters a product by category, since the category is a foriegn key
    filter_backends = [filters.SearchFilter]    #http://yourdomain.com/books/?category=some_category, this is how filtering done on browther
    filterset_class = ProductFilter
