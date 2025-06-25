from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MamaMbogaViewSet, CustomerViewSet, OrderViewSet, OrderItemViewSet,PaymentViewSet,CartViewSet,VendorReviewSet
# from .views import CustomerViewSet


router= DefaultRouter()
router.register(r"Mamamboga",MamaMbogaViewSet,basename="mamamboga")
router.register(r"Customer",CustomerViewSet,basename="customer")
router.register(r"VendorReview",VendorReviewSet,basename="feedback")
router.register(r"Order",OrderViewSet,basename="order")
router.register(r"OrderItem",OrderItemViewSet,basename="orderitem")
router.register(r"Payment",PaymentViewSet,basename="payment")
router.register(r"Cart",CartViewSet,basename="cart")


urlpatterns = [
    path("",include(router.urls))
]

