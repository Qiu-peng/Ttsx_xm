from django.contrib import admin
from .models import UserInfo, UserAddressInfo
# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'userName', 'userPsw', 'userEmail', 'isValid', 'isActive']
class UserAddressInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'uName', 'uAddress', 'uPhone', 'user']

admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(UserAddressInfo, UserAddressInfoAdmin)