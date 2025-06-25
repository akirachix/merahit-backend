from django.shortcuts import render

from rest_framework import viewsets
from users.models import MamaMboga, Customer
from order.models import Order,OrderItem,Payment,Cart
from .serializers import MamaMbogaSerializer, CustomerSerializer,OrderSerializer,OrderItemSerializer,PaymentSerializer,CartSerializer
# from users.models import Customer
# from .serializers import CustomerSerializer



class MamaMbogaViewSet(viewsets.ModelViewSet):
    queryset=MamaMboga.objects.all()
    serializer_class=MamaMbogaSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

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
