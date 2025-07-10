from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Rol de usuario', {'fields': ('rol',)}),
    )
    list_display = ('username', 'email', 'rol', 'is_staff')

admin.site.register(User, CustomUserAdmin)
