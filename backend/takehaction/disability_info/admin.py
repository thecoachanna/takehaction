from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, EmergencyContact


@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
