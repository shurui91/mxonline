from django.shortcuts import render
from django.views.generic.base import View

from MxOnline.apps.organizations.models import CourseOrg
from MxOnline.settings import MEDIA_URL


class OrgView(View):
    def get(self, request, *args, **kwargs):
        all_orgs = CourseOrg.objects.all()
        return render(request, 'org-list.html', {
            "all_orgs": all_orgs,
            "MEDIA_URL": MEDIA_URL,
        })
