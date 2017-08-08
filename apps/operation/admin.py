from django.contrib import admin
from .models import UserAsk,CourseComments,UserCourse,UserFavorite,UserMessage
# Register your models here.
class UserAskAdmin(admin.ModelAdmin):
    list_display=['mobile','name','add_time']
    search_fields=['mobile','name']
    list_filter=['mobile','name','add_time']
class CourseCommentsAdmin(admin.ModelAdmin):
    list_display=['user','course','comments']
    search_fields=['user','course','comments']
    list_filter=['user','course','comments']
class UserFavoriteAdmin(admin.ModelAdmin):
    list_display=['user','fav_id','add_time']
    search_fields=['user','fav_id']
    list_filter=['user','fav_id','add_time']
class UserMessageAdmin(admin.ModelAdmin):
    list_display=['user','message','add_time']
    search_fields=['user','message']
    list_filter=['user','message','add_time']
class UserCourseAdmin(admin.ModelAdmin):
    list_display=['user','course','add_time']
    search_fields=['user','course']
    list_filter=['user','course','add_time']

admin.site.register(UserAsk,UserAskAdmin)
admin.site.register(CourseComments,CourseCommentsAdmin)
admin.site.register(UserFavorite,UserFavoriteAdmin)
admin.site.register(UserMessage,UserMessageAdmin)
admin.site.register(UserCourse,UserCourseAdmin)