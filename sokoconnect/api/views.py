from django.shortcuts import render

from rest_framework import viewsets
from users.models import MamaMboga, Customer
from inventory.models import Product,Discount
from .serializers import MamaMbogaSerializer, CustomerSerializer,ProductSerializer,DiscountSerializer
# from users.models import Customer
# from .serializers import CustomerSerializer



class MamaMbogaViewSet(viewsets.ModelViewSet):
    queryset=MamaMboga.objects.all()
    serializer_class=MamaMbogaSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class DiscountViewSet(viewsets.ModelViewSet):
    queryset=Discount.objects.all()
    serializer_class=DiscountSerializer
# Create your views here.
