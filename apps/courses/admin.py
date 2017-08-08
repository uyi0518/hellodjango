from django.contrib import admin
from .models import Course,Lesson,Video,CourseResource

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display=['desc','detail','degree']
    search_fields=['desc','detail','degree']
    list_filter=['desc','detail','degree']
class LessonAdmin(admin.ModelAdmin):
    list_display=['name','course','add_time']
    search_fields=['name','course']
    list_filter=['name','course','add_time']
class VideoAdmin(admin.ModelAdmin):
    list_display=['name','lesson','add_time']
    search_fields=['name','lesson']
    list_filter=['name','lesson','add_time']
class CourseResourceAdmin(admin.ModelAdmin):
    list_display=['name','course','add_time']
    search_fields=['name','course']
    list_filter=['name','course','add_time']

admin.site.register(Course,CourseAdmin)
admin.site.register(Lesson,LessonAdmin)
admin.site.register(Video,VideoAdmin)
admin.site.register(CourseResource,CourseResourceAdmin)