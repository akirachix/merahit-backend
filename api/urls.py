from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    OrderViewSet, OrderItemViewSet, PaymentViewSet, CartViewSet,
    UsersViewSet, ProductViewSet, DiscountViewSet, ReviewViewSet,
    daraja_callback,
    STKPushView, Login, Signup
)
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r"orders", OrderViewSet, basename="order")
router.register(r"order-items", OrderItemViewSet, basename="orderitem")
router.register(r"payments", PaymentViewSet, basename="payment")
router.register(r"carts", CartViewSet, basename="cart")
router.register(r"users", UsersViewSet, basename="users")
router.register(r"products", ProductViewSet, basename="product")
router.register(r"discounts", DiscountViewSet, basename="discount")
router.register(r"reviews", ReviewViewSet, basename="review")

urlpatterns = [
    path("", include(router.urls)),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('daraja/stk-push/', STKPushView.as_view(), name='daraja-stk-push'),
    path('daraja/callback/', daraja_callback, name='daraja-callback'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
