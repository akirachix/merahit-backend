from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import UserCreationWithPasswordForm
from .models import Users
class UserAdmin(BaseUserAdmin):
    add_form = UserCreationWithPasswordForm
    form = UserCreationWithPasswordForm
    model = Users
    list_display = ('phone_number', 'full_name', 'usertype', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'usertype')
    search_fields = ('phone_number', 'full_name')
    ordering = ('full_name',)
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        (_('Personal info'), {'fields': ('full_name', 'usertype', 'address', 'latitude', 'longitude', 'profile_picture')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password', 'full_name', 'usertype'),
        }),
    )
admin.site.register(Users, UserAdmin)






