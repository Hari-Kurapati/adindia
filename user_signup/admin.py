from django.contrib import admin
from .models import Users

# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user_name',
        'user_phone',
        'user_email'
    ]

admin.site.register(Users, UsersAdmin)
