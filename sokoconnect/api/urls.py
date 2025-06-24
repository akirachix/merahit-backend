from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MamaMbogaViewSet, CustomerViewSet
# from .views import CustomerViewSet


router= DefaultRouter()
router.register(r"Mamamboga",MamaMbogaViewSet,basename="mamamboga")
router.register(r"Customer",CustomerViewSet,basename="customer")

urlpatterns = [
    path("",include(router.urls))
]

