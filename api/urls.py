from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    OrderViewSet, OrderItemViewSet, PaymentViewSet, CartViewSet,
    UsersViewSet, ProductViewSet, DiscountViewSet, ReviewViewSet,
 daraja_callback,
 STKPushView,Login,Signup
)
from . import views
from rest_framework.authtoken.views import obtain_auth_token
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
    path('signup/', Signup.as_view(), name='signup'),
     path('login/', Login.as_view(),name= 'Login'),
    path('daraja/stk-push/', STKPushView.as_view(), name='daraja-stk-push'),
    path('daraja/callback/', daraja_callback, name='daraja-callback'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]