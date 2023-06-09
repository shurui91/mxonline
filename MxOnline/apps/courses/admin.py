from django.contrib import admin

from MxOnline.apps.courses.models import Course, Lesson, Video, CourseResource, CourseTag


class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "desc", "detail", "degree", "learn_times", "students"]
    search_fields = ["name", "desc", "detail", "degree", "students"]
    list_filter = ["name", "desc", "detail", "degree", "learn_times", "students"]
    list_editable = ["desc", "degree"]


class LessonAdmin(admin.ModelAdmin):
    list_display = ["course", "name", "add_time"]
    search_fields = ["course", "name"]
    list_filter = ["course", "name", "add_time"]


class VideoAdmin(admin.ModelAdmin):
    list_display = ["lesson", "name", "add_time"]
    search_fields = ["lesson", "name"]
    list_filter = ["lesson", "name", "add_time"]


class CourseResourceAdmin(admin.ModelAdmin):
    list_display = ["course", "name", "download", "add_time"]
    search_fields = ["course", "name", "download"]
    list_filter = ["course", "name", "download", "add_time"]


class CourseTagAdmin(admin.ModelAdmin):
    list_display = ["course", "tag", "add_time"]
    search_fields = ["course", "tag"]
    list_filter = ["course", "tag", "add_time"]


admin.site.site_header = '幕课网管理后台'  # sidebar title
admin.site.site_title = '大江狗'  # tab title
admin.site.index_title = '大江狗管理后台'
# admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(CourseResource, CourseResourceAdmin)
admin.site.register(CourseTag, CourseTagAdmin)
