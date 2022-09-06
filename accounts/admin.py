from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    list_display = ['username', 'age','email', 'is_staff', ]
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = (UserAdmin.fieldsets + (
        (None, {'fields': ('age', )}),
         ))
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age', )}),
         )


admin.site.register(CustomUser, CustomUserAdmin)
