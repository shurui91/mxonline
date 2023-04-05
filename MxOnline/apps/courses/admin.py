from django.contrib import admin

from MxOnline.apps.courses.models import Course


class CourseAdmin(admin.ModelAdmin):
    pass


# admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Course, CourseAdmin)
