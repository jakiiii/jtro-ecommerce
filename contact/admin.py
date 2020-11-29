from django.contrib import admin
from .models import UserMessage, Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['office_address', 'phone', 'email', 'active']


@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'timestamp']
