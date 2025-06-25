from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import viewSet


router= DefaultRouter()
router.register(r"Review",viewSet,basename="feedback")



urlpatterns = [
   path("",include(router.urls))
]
