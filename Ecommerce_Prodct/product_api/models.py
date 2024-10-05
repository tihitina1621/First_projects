from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=250)

class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.CharField(max_length=20)
    stock_quantity = models.IntegerField()
    image_url = models.ImageField()
    Created_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

products = Product.objects.prefetch_related('category')
#separate query will be performed 

