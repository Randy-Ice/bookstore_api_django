from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
# Register your models here.



@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    ordering = ('email',)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("first_name",'last_name','email',  "usable_password", "password1", "password2"),
            },

        ),
    )
