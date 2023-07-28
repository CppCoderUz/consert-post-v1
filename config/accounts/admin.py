from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class _User(UserAdmin):
    list_display = ['username', 'last_name', 'first_name', 'email', 'is_active', 'is_staff', 'is_superuser']
    

