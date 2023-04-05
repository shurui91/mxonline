from django.contrib import admin

from MxOnline.apps.organizations.models import Teacher, CourseOrg, City


class TeacherAdmin(admin.ModelAdmin):
    pass


class CourseOrgAdmin(admin.ModelAdmin):
    pass


class CityAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "desc"]
    search_fields = ["name", "desc"]


# admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(CourseOrg, CourseOrgAdmin)
admin.site.register(City, CityAdmin)
