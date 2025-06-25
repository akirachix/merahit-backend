from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewSet



router= DefaultRouter()
router.register(r"Review",ReviewSet,basename="feedback")



urlpatterns = [
    path("",include(router.urls))
]

