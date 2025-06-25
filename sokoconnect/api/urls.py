from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  OrderViewSet, OrderItemViewSet,PaymentViewSet,CartViewSet, UsersViewSet,ProductViewSet , DiscountViewSet

router= DefaultRouter()
router.register(r"Order",OrderViewSet,basename="order")
router.register(r"OrderItem",OrderItemViewSet,basename="orderitem")
router.register(r"Payment",PaymentViewSet,basename="payment")
router.register(r"Cart",CartViewSet,basename="cart")
router.register(r'users', UsersViewSet, basename='users')
router.register(r"Product",ProductViewSet,basename="product")
router.register(r"Discount",DiscountViewSet,basename="discount")

urlpatterns = [
    path("",include(router.urls))
]

