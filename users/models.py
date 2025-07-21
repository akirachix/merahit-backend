from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.exceptions import ValidationError
class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The Phone number must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(phone_number, password, **extra_fields)
class Users(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('vendor', 'Vendor'),
    )
    phone_number = models.CharField(max_length=13, unique=True)
    first_name = models.CharField(max_length=50, default='Unknown')
    last_name = models.CharField(max_length=50, default='Unknown')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')
    address = models.CharField(max_length=300, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    user_image = models.URLField(max_length=1500, null=True, blank=True)
    till_number = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    def clean(self):
        if self.role == 'vendor' and not self.till_number:
            raise ValidationError({'till_number': 'Vendors must have a till number.'})
        if self.role == 'customer' and self.till_number:
            raise ValidationError({'till_number': 'Customers should not have a till number.'})
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()
    def get_short_name(self):
        return self.first_name or self.phone_number
    def __str__(self):
        full_name = self.get_full_name()
        return full_name if full_name else self.phone_number
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ['first_name', 'last_name']
        indexes = [
            models.Index(fields=['phone_number']),
            models.Index(fields=['role']),
        ]
    def save(self, *args, **kwargs):
        if not self.phone_number.startswith('+'):
            raise ValidationError("Phone number must start with '+' followed by the country code.")
        super().save(*args, **kwargs)
        if self.role == 'vendor' and not self.till_number:
            raise ValidationError("Vendors must have a till number.")
        if self.role == 'customer' and self.till_number:
            raise ValidationError("Customers should not have a till number.")
        super().save(*args, **kwargs)
        return self