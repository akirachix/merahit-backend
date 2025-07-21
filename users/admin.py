from django.contrib import admin
from .models import Users
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from rest_framework.authtoken.models import Token
from django.utils.translation import gettext_lazy as _
from .forms import UserCreationWithPasswordForm
class UserAdmin(BaseUserAdmin):
    add_form = UserCreationWithPasswordForm
    model = Users
    list_display = ('first_name', 'last_name', 'role', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'role')
    search_fields = ('first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'role', 'address', 'latitude', 'longitude','user_image','till_number')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password', 'first_name', 'last_name', 'role','till_number'),
        }),
    )
    ordering = ('first_name',)
admin.site.register(Users, UserAdmin)