from rest_framework import serializers
from geolocation.models import GeoLocation

class GeoLocationSerializer(serializers.ModelSerializer):
   class Meta:
       model = GeoLocation
       fields = ['id', 'name', 'latitude', 'longitude', 'address']