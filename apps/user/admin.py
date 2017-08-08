from django.contrib import admin
from .models import EmailVerifyRecord,Banner

# Register your models here.

class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display=['code','email','send_type','send_time']
    search_fields=['code','email','send_type']
    list_filter=['code','email','send_type','send_time']
class BannerAdmin(admin.ModelAdmin):

    list_display=['title','image','index','add_time','url']
    search_fields=['title','image','index','url']
    list_filter=['title','image','index','add_time','url']

admin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
admin.site.register(Banner,BannerAdmin)


