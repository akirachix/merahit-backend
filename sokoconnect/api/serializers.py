from rest_framework import serializers
from order.models import Order, Payment, Cart, OrderItem
from users.models import Users, Customer, MamaMboga
from inventory.models import Product, Discount
from reviews.models import Review

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'full_name', 'phone_number', 'latitude', 'longitude', 'profile_picture', 'created_at', 'updated_at', 'usertype', 'is_loyal']

class MamaMbogaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MamaMboga
        fields = ['id', 'full_name', 'phone_number', 'latitude', 'longitude', 'profile_picture', 'created_at', 'updated_at', 'usertype']

class UsersSerializer(serializers.ModelSerializer):
    # This will delegate serialization to Customer or MamaMboga serializer based on usertype
    def to_representation(self, instance):
        try:
            if instance.usertype == 'customer' and hasattr(instance, 'customer'):
                serializer = CustomerSerializer(instance.customer)
            elif instance.usertype == 'mamamboga' and hasattr(instance, 'mamamboga'):
                serializer = MamaMbogaSerializer(instance.mamamboga)
            else:
                return super().to_representation(instance)
            return serializer.data
        except (Customer.DoesNotExist, MamaMboga.DoesNotExist):
            return super().to_representation(instance)

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
            'created_at',
            'updated_at',
            'usertype',
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
        fields = "__all__"

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
        model = Discount  # Fixed: was mistakenly set to Cart before
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):
    # Nest vendor and customer serializers to show their details instead of just IDs
    vendor = MamaMbogaSerializer(read_only=True)
    customer = CustomerSerializer(read_only=True)

    # Allow write operations with IDs for vendor and customer
    vendor_id = serializers.PrimaryKeyRelatedField(queryset=MamaMboga.objects.all(), source='vendor', write_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), source='customer', write_only=True)

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
