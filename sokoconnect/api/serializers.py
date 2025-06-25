from rest_framework import serializers
from inventory.models import Product,Discount

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Discount
        fields="__all__"
