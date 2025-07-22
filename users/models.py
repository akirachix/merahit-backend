from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The phone number must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user
    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('usertype', 'admin')  

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        return self.create_user(phone_number, password, **extra_fields)

class Users(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        ('customer', 'Customer'),
        ('mamamboga', 'Mama Mboga'),
        ('admin', 'Admin'), 
    )
    full_name = models.CharField(max_length=100, default='Unknown User')
    phone_number = models.CharField(max_length=15, unique=True)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    profile_picture = models.URLField(max_length=200, default='https://example.com/default-profile-pic.jpg', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    usertype = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='mamamboga')
    address = models.CharField(max_length=300, default="Nairobi, Kenya")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.full_name

class Customer(Users):
    is_loyal = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.usertype = 'customer'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Welcome {self.full_name}"

class MamaMboga(Users):
    working_days = models.CharField(max_length=200)
    working_hours = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.usertype = 'mamamboga'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Welcome {self.full_name}"
