from rest_framework import serializers
from users.models import MamaMboga
from users.models import Customer
from inventory.models import Product,Discount



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