from django.shortcuts import render
from django.views.generic.base import View

from MxOnline.apps.organizations.models import CourseOrg, City
from MxOnline.settings import MEDIA_URL


class OrgView(View):
    def get(self, request, *args, **kwargs):
        # 从数据库获取数据
        all_orgs = CourseOrg.objects.all()
        all_cities = City.objects.all()

        # 对课程机构进行筛选
        category = request.GET.get("ct", "")
        if category:
            all_orgs = all_orgs.filter(category=category)

        org_nums = all_orgs.count()

        return render(request, 'org-list.html', {
            "all_orgs": all_orgs,
            "org_nums": org_nums,
            "all_cities": all_cities,
        })
