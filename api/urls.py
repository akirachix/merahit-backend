from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    OrderViewSet, OrderItemViewSet, PaymentViewSet, CartViewSet,
    UsersViewSet, ProductViewSet, DiscountViewSet, ReviewViewSet,AdminViewSet,
 daraja_callback,
 STKPushView,
)
from . import views
from rest_framework.authtoken.views import obtain_auth_token



router = DefaultRouter()
router.register(r"order", OrderViewSet, basename="order")
router.register(r"orderItem", OrderItemViewSet, basename="orderitem")
router.register(r"payment", PaymentViewSet, basename="payment")
router.register(r"cart", CartViewSet, basename="cart")
router.register(r"users", UsersViewSet, basename="users")
router.register(r"admin", AdminViewSet, basename="Admin")
router.register(r"product", ProductViewSet, basename="product")
router.register(r"discount", DiscountViewSet, basename="discount")
router.register(r"review", ReviewViewSet, basename="feedback")

urlpatterns = [
    path("", include(router.urls)),
     path('login/', obtain_auth_token),  
    path('daraja/stk-push/', STKPushView.as_view(), name='daraja-stk-push'),
    path('daraja/callback/', daraja_callback, name='daraja-callback'),
  
]