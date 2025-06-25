from django.shortcuts import render

from rest_framework import viewsets
from inventory.models import Product,Discount
from .serializers import ProductSerializer,DiscountSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class DiscountViewSet(viewsets.ModelViewSet):
    queryset=Discount.objects.all()
    serializer_class=DiscountSerializer

