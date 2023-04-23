from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

from MxOnline.apps.operations.forms import UserFavForm
from MxOnline.apps.operations.models import UserFavorite
from MxOnline.apps.courses.models import Course
from MxOnline.apps.organizations.models import CourseOrg, Teacher


class AddFavView(View):
    def post(self, request, *args, **kwargs):
        """
        用户收藏，用户取消收藏
        """
        user_fav_form = UserFavForm(request.POST)
        # 如果用户未登录，不能收藏
        if not request.user.is_authenticated:
            return JsonResponse({
                "status": "fail",
                "msg": "用户未登录",
            })

        user_fav_form = UserFavForm(request.POST)
        if user_fav_form.is_valid():
            fav_id = user_fav_form.cleaned_data["fav_id"]
            fav_type = user_fav_form.cleaned_data["fav_type"]

            # 是否已经收藏
            existed_records = UserFavorite.objects.filter(user=request.user, fav_id=fav_id, fav_type=fav_type)
            # 如果收藏过了但是页面显示未收藏，再点击的时候就要取消收藏
            if existed_records:
                existed_records.delete()

                # 被收藏的是什么东西，课程，机构，还是老师
                if fav_type == 1:
                    course = Course.objects.get(id=fav_id)
                    course.fav_nums -= 1
                    course.save()
                elif fav_type == 2:
                    course_org = CourseOrg.objects.get(id=fav_id)
                    course_org.fav_nums -= 1
                    course_org.save()
                elif fav_type == 3:
                    teacher = Teacher.objects.get(id=fav_id)
                    teacher.fav_nums -= 1
                    teacher.save()

                return JsonResponse({
                    "status": "success",
                    "msg": "收藏",
                })
            else:
                user_fav = UserFavorite()
                user_fav.fav_id = fav_id
                user_fav.fav_type = fav_type
                user_fav.user = request.user
                user_fav.save()

                return JsonResponse({
                    "status": "success",
                    "msg": "已收藏",
                })
        else:
            return JsonResponse({
                "status": "fail",
                "msg": "参数错误",
            })
