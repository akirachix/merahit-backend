from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MamaMbogaViewSet, CustomerViewSet, VendorReviewSet
# from .views import CustomerViewSet


router= DefaultRouter()
router.register(r"Mamamboga",MamaMbogaViewSet,basename="mamamboga")
router.register(r"Customer",CustomerViewSet,basename="customer")
router.register(r"VendorReview",VendorReviewSet,basename="feedback")

urlpatterns = [
    path("",include(router.urls))
]

