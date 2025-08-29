from rest_framework import serializers
from .models import Product, Order, MenuItem
from django.contrib.auth import get_user_model

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

User = get_user_model()
class StaffRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'role']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password'],
            role = validated_data['role']
        )
        return user

