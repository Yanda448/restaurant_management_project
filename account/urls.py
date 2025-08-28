from django.urls import path, include
from .views import ProductViewSet, OrderViewSet
from rest_framework.routers import DefaultRouter

#Creating a router and register the viewsets
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'orders', OrderViewSet, basename='order')
urlpatterns = [
    path('', include(router.urls)),
]