from django.urls import path, include
from . import views
from .views import CategoryViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'Catagory', CategoryViewSet)
router.register(r'Product', ProductViewSet)

urlpatterns = [
    #path('', views.index, name='index'),
    path('api/', include(router.urls)),
]