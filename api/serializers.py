from rest_framework import serializers
from order.models import Order, Payment, Cart, OrderItem
from users.models import Users
from inventory.models import Product, Discount
from reviews.models import Review

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
            'full_name',
            'phone_number',
            'password',
            'latitude',
            'longitude',
            'profile_picture',
            'usertype',
            'address',
            'is_active',
            'is_staff',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class DiscountSerializer(serializers.ModelSerializer):
    vendor = UsersSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    vendor_id = serializers.PrimaryKeyRelatedField(
        queryset=Users.objects.filter(usertype='mamamboga'),
        source='vendor',
        write_only=True
    )
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product',
        write_only=True
    )

    class Meta:
        model = Discount
        fields = [
            'id',
            'old_price',
            'new_price',
            'start_date',
            'end_date',
            'created_at',
            'vendor',
            'product',
            'vendor_id',
            'product_id',
        ]
        read_only_fields = ['vendor', 'product', 'created_at']


class ReviewSerializer(serializers.ModelSerializer):
    vendor = UsersSerializer(read_only=True)
    customer = UsersSerializer(read_only=True)
    vendor_id = serializers.PrimaryKeyRelatedField(
        queryset=Users.objects.filter(usertype='mamamboga'),
        source='vendor',
        write_only=True
    )
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Users.objects.filter(usertype='customer'),
        source='customer',
        write_only=True
    )

    class Meta:
        model = Review
        fields = ['id', 'vendor', 'customer', 'vendor_id', 'customer_id', 'rating', 'comment', 'created_at']
        read_only_fields = ['vendor', 'customer', 'created_at']


class OrderSerializer(serializers.ModelSerializer):
    vendor = UsersSerializer(read_only=True)
    customer = UsersSerializer(read_only=True)
    vendor_id = serializers.PrimaryKeyRelatedField(
        queryset=Users.objects.filter(usertype='mamamboga'),
        source='vendor',
        write_only=True
    )
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Users.objects.filter(usertype='customer'),
        source='customer',
        write_only=True
    )

    class Meta:
        model = Order
        fields = [
            'id',
            'vendor',
            'customer',
            'vendor_id',
            'customer_id',
            'order_date',
            'status',
            'total_amount',
            'created_at'
        ]
        read_only_fields = ['vendor', 'customer', 'created_at']


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
