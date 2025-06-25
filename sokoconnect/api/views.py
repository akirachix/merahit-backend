from django.shortcuts import render

from rest_framework import viewsets
from users.models import MamaMboga, Customer


from order.models import Order,OrderItem,Payment,Cart,VendorReview,Product,Discount
from .serializers import MamaMbogaSerializer, CustomerSerializer,OrderSerializer,OrderItemSerializer,PaymentSerializer,CartSerializer,VendorReviewSerializer,ProductSerializer,DiscountSerializer


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
=======
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



class VendorReviewSet(viewsets.ModelViewSet):
    queryset= VendorReview.objects.all()
    serializer_class= VendorReviewSerializer
