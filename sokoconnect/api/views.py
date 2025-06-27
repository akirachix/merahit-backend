from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from order.models import Order,OrderItem,Payment,Cart
from inventory.models import Product,Discount
from users.models import Users, Customer, MamaMboga
from .serializers import UsersSerializer, MamaMbogaSerializer, CustomerSerializer,ProductSerializer,DiscountSerializer,OrderSerializer,OrderItemSerializer,PaymentSerializer,CartSerializer

from reviews.models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset= Review.objects.all()
    serializer_class= ReviewSerializer

from reviews.models import Review
from .serializers import ReviewSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer


from reviews.models import Review
from .serializers import ReviewSerializer

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

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class DiscountViewSet(viewsets.ModelViewSet):
    queryset=Discount.objects.all()
    serializer_class=DiscountSerializer
    

class viewSet(viewsets.ModelViewSet):
   queryset= Review.objects.all()
   serializer_class= ReviewSerializer



class ReviewViewSet(viewsets.ModelViewSet):
    queryset= Review.objects.all()
    serializer_class= ReviewSerializer
