from rest_framework import serializers
from order.models import Order, Payment, Cart, OrderItem
from users.models import Users, Customer, MamaMboga
from inventory.models import Product, Discount
from reviews.models import Review

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'full_name', 'phone_number', 'latitude', 'longitude', 'profile_picture', 'created_at', 'updated_at', 'usertype', 'is_loyal','address' ]

class MamaMbogaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MamaMboga
        fields = ['id', 'full_name', 'phone_number', 'latitude', 'longitude', 'profile_picture', 'created_at', 'updated_at', 'usertype','address' ]

class UsersSerializer(serializers.ModelSerializer):
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
        model = Discount  
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):
    vendor = MamaMbogaSerializer(read_only=True)
    customer = CustomerSerializer(read_only=True)
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

class STKPushSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    order_item= serializers.CharField()
    account_reference = serializers.CharField()
    transaction_desc = serializers.CharField()


class MamaMbogaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MamaMboga
        fields = '__all__'
    def create(self, validated_data):
        address_description = validated_data.get('address_description')
        if address_description:
            latitude, longitude = forward_geocode(address_description)
            if latitude is not None and longitude is not None:
                validated_data['location_latitude'] = latitude
                validated_data['location_longitude'] = longitude
            else:
                raise serializers.ValidationError("Geocoding failed for the provided address")
        return super().create(validated_data)
    def update(self, instance, validated_data):
        address_description = validated_data.get('address_description', instance.address_description)
        if address_description and address_description != instance.address_description:
            latitude, longitude = forward_geocode(address_description)
            if latitude is not None and longitude is not None:
                validated_data['location_latitude'] = latitude
                validated_data['location_longitude'] = longitude
            else:
                raise serializers.ValidationError("Geocoding failed for the provided address")
        return super().update(instance, validated_data)

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
    def create(self, validated_data):
        address_description = validated_data.get('address_description')
        if address_description:
            latitude, longitude = forward_geocode(address_description)
            if latitude is not None and longitude is not None:
                validated_data['location_latitude'] = latitude
                validated_data['location_longitude'] = longitude
            else:
                raise serializers.ValidationError("Geocoding failed for the provided address")
        return super().create(validated_data)
    def update(self, instance, validated_data):
        address_description = validated_data.get('address_description', instance.address_description)
        if address_description and address_description != instance.address_description:
            latitude, longitude = forward_geocode(address_description)
            if latitude is not None and longitude is not None:
                validated_data['location_latitude'] = latitude
                validated_data['location_longitude'] = longitude
            else:
                raise serializers.ValidationError("Geocoding failed for the provided address")
        return super().update(instance, validated_data)
