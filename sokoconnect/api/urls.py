from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet,ProductViewSet , DiscountViewSet

router = DefaultRouter()
router.register(r'users', UsersViewSet, basename='users')
router.register(r"Product",ProductViewSet,basename="product")
router.register(r"Discount",DiscountViewSet,basename="discount")

urlpatterns = [
    path("",include(router.urls))
]

