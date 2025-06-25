from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MamaMbogaViewSet, CustomerViewSet , ProductViewSet , DiscountViewSet
# from .views import CustomerViewSet


router= DefaultRouter()
router.register(r"Mamamboga",MamaMbogaViewSet,basename="mamamboga")
router.register(r"Customer",CustomerViewSet,basename="customer")
router.register(r"Product",ProductViewSet,basename="product")
router.register(r"Discount",DiscountViewSet,basename="discount")

urlpatterns = [
    path("",include(router.urls))
]

