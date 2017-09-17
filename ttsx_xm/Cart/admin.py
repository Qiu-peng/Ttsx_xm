from django.contrib import admin
from .models import CartInfo

# Register your models here.

class CartInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'goods', 'count']

admin.site.register(CartInfo, CartInfoAdmin)