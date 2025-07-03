from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    OrderViewSet, OrderItemViewSet, PaymentViewSet, CartViewSet,
    UsersViewSet, ProductViewSet, DiscountViewSet, ReviewViewSet,
    STKPushView, daraja_callback
)
from . import views




router = DefaultRouter()
router.register(r"Order", OrderViewSet, basename="order")
router.register(r"OrderItem", OrderItemViewSet, basename="orderitem")
router.register(r"Payment", PaymentViewSet, basename="payment")
router.register(r"Cart", CartViewSet, basename="cart")
router.register(r"users", UsersViewSet, basename="users")
router.register(r"Product", ProductViewSet, basename="product")
router.register(r"Discount", DiscountViewSet, basename="discount")
router.register(r"Review", ReviewViewSet, basename="feedback")

urlpatterns = [
    path("", include(router.urls)),
    path('daraja/stk-push/', STKPushView.as_view(), name='daraja-stk-push'),
    path('daraja/callback/', daraja_callback, name='daraja-callback'),
    path('geocode/', views.geocode_view, name='geocode'),
    path('reverse-geocode/', views.reverse_geocode_view, name='reverse_geocode'),
]