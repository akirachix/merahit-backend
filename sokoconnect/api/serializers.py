from rest_framework import serializers
from reviews.models import VendorReview


 
class VendorReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=VendorReview
        fields="__all__"
  