from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  OrderViewSet, OrderItemViewSet,PaymentViewSet,CartViewSet
# from .views import CustomerViewSet

router= DefaultRouter()
router.register(r"Order",OrderViewSet,basename="order")
router.register(r"OrderItem",OrderItemViewSet,basename="orderitem")
router.register(r"Payment",PaymentViewSet,basename="payment")
router.register(r"Cart",CartViewSet,basename="cart")

urlpatterns = [
    path("",include(router.urls))
]

