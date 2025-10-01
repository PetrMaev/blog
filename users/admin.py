from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "login", "email", "born_date", "phone_number", "is_active")
    search_fields = ("email",)
