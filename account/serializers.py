from rest_framework import serializers
from .models import Product, Order, MenuItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name") #Show category name

    class Meta:
        model = MenuItem
        fields = ["id", "name", "category"]
