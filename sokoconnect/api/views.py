from django.shortcuts import render

from rest_framework import viewsets
from order.models import Order,OrderItem,Payment,Cart
from .serializers import OrderSerializer,OrderItemSerializer,PaymentSerializer,CartSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer
# Create your views here.
