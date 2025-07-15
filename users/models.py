from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Users(models.Model):
    USER_TYPE_CHOICES = (
        ('customer', 'Customer'),
        ('mamamboga', 'Mama Mboga'),
        ('admin','Admin'),
    )

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=8)
    latitude = models.FloatField()
    longitude = models.FloatField()
    profile_picture = models.URLField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    usertype = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default="mamamboga")
    address = models .CharField(max_length=300, default="Nairobi, Kenya")

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Customer(Users):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_loyal = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.usertype = 'customer'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name}"

class MamaMboga(Users):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    working_days = models.CharField(max_length=200)
    working_hours = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.usertype = 'mamamboga'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name}"

###
class Admin(models.Model):
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=8)



