from django.shortcuts import render

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from inventory.models import Product,Discount
from users.models import Users, Customer, MamaMboga
from .serializers import UsersSerializer, MamaMbogaSerializer, CustomerSerializer,ProductSerializer,DiscountSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['usertype'] 

class MamaMbogaViewSet(viewsets.ModelViewSet):
    queryset = MamaMboga.objects.all()
    serializer_class = MamaMbogaSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
# Create your views here


class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class DiscountViewSet(viewsets.ModelViewSet):
    queryset=Discount.objects.all()
    serializer_class=DiscountSerializer
    