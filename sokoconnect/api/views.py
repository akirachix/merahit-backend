from django.shortcuts import render

from rest_framework import viewsets
from users.models import MamaMboga, Customer
from reviews.models import VendorReview
from .serializers import MamaMbogaSerializer, CustomerSerializer,VendorReviewSerializer
# from users.models import Customer
# from .serializers import CustomerSerializer



class MamaMbogaViewSet(viewsets.ModelViewSet):
    queryset=MamaMboga.objects.all()
    serializer_class=MamaMbogaSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
# Create your views here.


class VendorReviewSet(viewsets.ModelViewSet):
    queryset= VendorReview.objects.all()
    serializer_class= VendorReviewSerializer
