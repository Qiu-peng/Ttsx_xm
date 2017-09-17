from django.contrib import admin
from .models import OrderInfo, OrderDetailInfo

# Register your models here.

class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ['oid', 'user', 'odate', 'oIsPay' ,'ototal' ,'oaddress']
class OrderDetailInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'goods', 'order', 'price', 'count']

admin.site.register(OrderInfo, OrderInfoAdmin)
admin.site.register(OrderDetailInfo, OrderDetailInfoAdmin)