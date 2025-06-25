from rest_framework import serializers
from users.models import MamaMboga

from reviews.models import VendorReview

from users.models import Customer


class MamaMbogaSerializer(serializers.ModelSerializer):
    class Meta:
        model=MamaMboga
        fields="__all__"

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields="__all__"

class VendorReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=VendorReview
        fields="__all__"
        