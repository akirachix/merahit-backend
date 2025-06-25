from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorReviewSet



router= DefaultRouter()
router.register(r"VendorReview",VendorReviewSet,basename="feedback")



urlpatterns = [
    path("",include(router.urls))
]

