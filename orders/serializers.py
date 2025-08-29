from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'items', 'status']
        read_only_fields = ['status']

class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']
    
    def validate_status(self, value):
        order = self.instance
        if not order.can_update_to(value):
            raise serializers.ValidationError(
                f"Invalid status transition: {order.status} -> {value}"
            )
        return value
