from django.shortcuts import render

from rest_framework import viewsets
from users.models import MamaMboga, Customer
from order.models import Order,OrderItem,Payment,Cart
from .serializers import MamaMbogaSerializer, CustomerSerializer,OrderSerializer,OrderItemSerializer,PaymentSerializer,CartSerializer


class MamaMbogaViewSet(viewsets.ModelViewSet):
    queryset=MamaMboga.objects.all()
    serializer_class=MamaMbogaSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
