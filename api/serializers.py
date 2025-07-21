from rest_framework import serializers
from order.models import Order, Payment, Cart, OrderItem
from users.models import Users
from inventory.models import Product, Discount
from reviews.models import Review
from .daraja import DarajaAPI
from django.contrib.auth.models import User
class UsersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Users(**validated_data)
        user.set_password(password)
        user.save()
        return user
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
    class Meta:
        model = Users
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'password',
            'latitude',
            'longitude',
            'user_image',
            'role',
            'address',
            'till_number',
            'is_active',
            'is_staff',
        ]
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'status', 'amount',
            'merchant_request_id', 'checkout_request_id', 'result_code',
            'result_desc', 'mpesa_receipt_number', 'phone_number',
            'transaction_date', 'updated_at', 'order'
        ]
        read_only_fields = ['payment_id', 'created_at', 'updated_at']
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = "__all__"
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'vendor',
            'vendor_id',
            'customer',
            'customer_id',
            'rating',
            'comment',
            'created_at',
        ]
class STKPushSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    order_item = serializers.ListField()
    account_reference = serializers.CharField(max_length=12, default="TX12345")
    transaction_desc = serializers.CharField()
class DarajaAPISerializer(serializers.Serializer):
    class Meta:
        model = Payment
        fields = '__all__'