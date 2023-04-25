from django.shortcuts import render
from django.views.generic.base import View
from MxOnline.apps.courses.models import Course, CourseTag
from MxOnline.apps.operations.models import UserFavorite


class CourseLessonView(View):
    def get(self, request, course_id, *args, **kwargs):
        """获取课程章节信息"""
        course = Course.objects.get(id=int(course_id))
        course.click_nums += 1
        course.save()

        return render(request, "course-video.html", {
            "course": course,
        })


class CourseDetailView(View):
    def get(self, request, course_id, *args, **kwargs):
        """获取课程详情"""
        course = Course.objects.get(id=int(course_id))
        course.click_nums += 1
        course.save()

        # 获取收藏状态
        has_fav_course = False
        has_fav_org = False

        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True

        # 通过课程的tag做课程推荐
        # tag = course.tag
        # related_courses = []
        # if tag:
        #     related_courses = Course.objects.filter(tag=tag).exclude(id__in=[course.id])[:3]
        tags = course.coursetag_set.all()
        tag_list = [tag.tag for tag in tags]

        course_tags = CourseTag.objects.filter(tag__in=tag_list).exclude(course__id=course.id)
        # 为了避免两个课程有多个相同的tag
        related_courses = set()
        for course_tag in course_tags:
            related_courses.add(course_tag.course)

        return render(request, "course-detail.html", {
            "course": course,
            "has_fav_course": has_fav_course,
            "has_fav_org": has_fav_org,
            "course_tags": course_tags,
            "related_courses": related_courses,
        })


class CourseListView(View):
    def get(self, request, *args, **kwargs):
        """获取课程列表信息"""
        all_courses = Course.objects.order_by("-id")
        hot_courses = Course.objects.order_by("-click_nums")[:3]

        # 课程排序
        sort = request.GET.get("sort", "")
        if sort == "students":
            all_courses = all_courses.order_by("-students")
        elif sort == "hot":
            all_courses = all_courses.order_by("-click_nums")

        return render(request, "course-list.html", {
            "all_courses": all_courses,
            "sort": sort,
            "hot_courses": hot_courses,
        })
