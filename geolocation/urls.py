from django.urls import path
from .views import GeoLocationListView, NearbyVendor


urlpatterns = [
   path('locations/', GeoLocationListView.as_view(), name='location-list'),
   path('locations/add/', NearbyVendor.as_view(), name='location-add'),
]
