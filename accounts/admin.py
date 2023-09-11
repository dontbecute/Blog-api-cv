from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .forms import Createion , Change
from .models import CustomUser
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = Createion
    form = Change
    model = CustomUser

    list_display = ["email",
        "username",
        "name",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)
    
    
admin.site.register(CustomUser, CustomUserAdmin)