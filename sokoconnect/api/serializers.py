from rest_framework import serializers
from users.models import MamaMboga
from inventory.models import Product,Discount
from reviews.models import VendorReview

from users.models import Customer
from order.models import Order,Payment,Cart,OrderItem


class MamaMbogaSerializer(serializers.ModelSerializer):
    class Meta:
        model=MamaMboga
        fields="__all__"


        

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields="__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Discount
        fields="__all__"
=======
class VendorReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=VendorReview
        fields="__all__"
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields="__all__"

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        feilds="__all__"

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields="__all__"

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"

