from django.contrib import admin
from .models import TypeInfo, GoodsInfo
# Register your models here.

class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'ttile', 'isDelete']
class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'gtitle', 'gpic', 'gprice', 'idDelete', 'gunit', 'gclick', 'gkucun', 'gcontent', 'gtype']

admin.site.register(TypeInfo, TypeInfoAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)