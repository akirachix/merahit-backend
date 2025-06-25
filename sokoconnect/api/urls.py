from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet , DiscountViewSet




router= DefaultRouter()
router.register(r"Product",ProductViewSet,basename="product")
router.register(r"Discount",DiscountViewSet,basename="discount")

urlpatterns = [
    path("",include(router.urls))
]

