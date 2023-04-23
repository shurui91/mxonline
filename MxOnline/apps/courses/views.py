from django.shortcuts import render
from django.views.generic.base import View
from MxOnline.apps.courses.models import Course


class CourseListView(View):
    def get(self, request, *args, **kwargs):
        """获取课程列表信息"""
        all_courses = Course.objects.order_by("-id")

        # 课程排序
        sort = request.GET.get("sort", "")
        if sort == "students":
            all_courses = all_courses.order_by("-students")
        elif sort == "hot":
            all_courses = all_courses.order_by("-click_nums")

        return render(request, "course-list.html", {
            "all_courses": all_courses,
            "sort": sort,
        })
