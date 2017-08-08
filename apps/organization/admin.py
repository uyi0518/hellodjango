from django.contrib import admin
from .models import CityDict,CourseOrg,Techers

# Register your models here.

class CityDictAdmin(admin.ModelAdmin):
    list_display=['desc','name','add_time']
    search_fields=['desc','name']
    list_filter=['desc','name','add_time']
class CourseOrgAdmin(admin.ModelAdmin):
    list_display=['city','name','address']
    search_fields=['city','name','address']
    list_filter=['city','name','address']
class TechersAdmin(admin.ModelAdmin):
    list_display=['org','name','work_years']
    search_fields=['org','name','work_years']
    list_filter=['org','name','work_years']


admin.site.register(CityDict,CityDictAdmin)
admin.site.register(CourseOrg,CourseOrgAdmin)
admin.site.register(Techers,TechersAdmin)
