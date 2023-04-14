from django.shortcuts import render
from django.views.generic.base import View

from MxOnline.apps.organizations.models import CourseOrg, City
from MxOnline.settings import MEDIA_URL


class OrgView(View):
    def get(self, request, *args, **kwargs):
        # 从数据库获取数据
        all_orgs = CourseOrg.objects.all()
        all_cities = City.objects.all()

        # 通过机构类别对课程机构进行筛选
        # 这里默认值为空
        category = request.GET.get("ct", "")
        if category:
            all_orgs = all_orgs.filter(category=category)

        # 通过城市对课程机构进行筛选
        city_id = request.GET.get("city", "")
        if city_id:
            if city_id.isdigit():
                all_orgs = all_orgs.filter(city_id=int(city_id))

        # 对课程机构进行排序
        sort = request.GET.get("sort", "")
        if sort == "students":
            all_orgs = all_orgs.order_by("-students")
        elif sort == "course_nums":
            all_orgs = all_orgs.order_by("-course_nums")

        org_nums = all_orgs.count()

        return render(request, 'org-list.html', {
            "all_orgs": all_orgs,
            "org_nums": org_nums,
            "all_cities": all_cities,
            "category": category,
            "city_id": city_id,
            "sort": sort,
        })
