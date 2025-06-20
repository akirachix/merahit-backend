from django.db import models
from django.utils import timezone

class Users(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number= models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=8)
    latitude = models.FloatField()
    longitude = models.FloatField()
    profile_picture = models.URLField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class Customer(Users):
    is_loyal = models.BooleanField(default=False)
    def __str__ (self):
        return f"Welcome {self.full_name}"

class MamaMboga(Users):
    working_days = models.CharField(max_length=200)
    working_hours = models.CharField(max_length=200)
    def __str__(self):
        return f"Welcome {self.full_name}"