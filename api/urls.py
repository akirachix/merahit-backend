from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    OrderViewSet, OrderItemViewSet, PaymentViewSet, CartViewSet,
    UsersViewSet, ProductViewSet, DiscountViewSet, ReviewViewSet,  PaymentViewSet,
    # TestView, MakePayment, STKPushCallbackView, ApiRootView,
 daraja_callback,
 STKPushView,
)
from . import views
from .views import ForwardGeocodeView,ReverseGeocodeView
# from .views import api_forward_geocode,api_reverse_geocode





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
    # path('test/', TestView.as_view(), name='test'),
    # path('make-payment/', MakePayment.as_view(), name='make-payment'),
    # path('stkpush-callback/', STKPushCallbackView.as_view(), name='stkpush-callback'),
    # path('', ApiRootView.as_view(), name='api-root'),
    path('geocode/forward/', ForwardGeocodeView.as_view(), name='geocode-forward'),
    path('geocode/reverse/', ReverseGeocodeView.as_view(), name='geocode-reverse'),
    # path('forward-geocode/', views.api_forward_geocode, name='forward-geocode'),
    # path('reverse-geocode/', views.api_reverse_geocode, name='reverse-geocode'),
]