from django.shortcuts import render
from rest_framework import viewsets

from reviews.models import VendorReview
from .serializers import VendorReviewSerializer


class VendorReviewSet(viewsets.ModelViewSet):
    queryset= VendorReview.objects.all()
    serializer_class= VendorReviewSerializer