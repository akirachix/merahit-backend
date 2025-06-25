from rest_framework import serializers
from order.models import Order,Payment,Cart,OrderItem

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields="__all__"

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields="__all__"

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields="__all__"

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields="__all__"