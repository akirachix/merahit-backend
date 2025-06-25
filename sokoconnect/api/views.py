from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import viewSet

<<<<<<< feature/review-rating
=======
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from order.models import Order,OrderItem,Payment,Cart
from inventory.models import Product,Discount
from users.models import Users, Customer, MamaMboga
from .serializers import UsersSerializer, MamaMbogaSerializer, CustomerSerializer,ProductSerializer,DiscountSerializer,OrderSerializer,OrderItemSerializer,PaymentSerializer,CartSerializer

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
>>>>>>> develop

router= DefaultRouter()
router.register(r"Review",viewSet,basename="feedback")


<<<<<<< feature/review-rating

urlpatterns = [
   path("",include(router.urls))
]
=======
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class DiscountViewSet(viewsets.ModelViewSet):
    queryset=Discount.objects.all()
    serializer_class=DiscountSerializer
    
>>>>>>> develop
