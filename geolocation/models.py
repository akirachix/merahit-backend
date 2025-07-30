from django.db import models
from users.models import Users


class GeoLocation(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='geolocations')
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=255,null=True)

    def __str__(self):
        return f"{self.name} is a ({self.user.usertype})"