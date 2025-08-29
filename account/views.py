from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsManagerOrAdmin, IsWaiter, IsCashier
from .models import Product, Order, MenuItem
from .serializers import ProductSerializer, OrderSerializer, MenuItemSerializer
from rest_framework import generics

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsManagerOrAdmin] #only Manager/Admin

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsWaiter] #Only Waiter

class MenuListAPIView(generics.ListAPIView):
    queryset = MenuItem.objects.select_related("category").all()
    serializer_class = MenuItemSerializer
