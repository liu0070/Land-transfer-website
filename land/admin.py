from django.contrib import admin
from .models import Land,Image,Customer_Need


# Register your models here.
class LandAdmin(admin.ModelAdmin):
    list_display = ('location', 'type', 'size')
    search_fields = ('location', 'type', 'size')


admin.site.register(Land, LandAdmin)
admin.site.register(Image)
admin.site.register(Customer_Need)
admin.site.site_header = "土地流转后台管理平台"
admin.site.site_title = "信息后台管理"