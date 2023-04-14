from django.urls import re_path as url
from MxOnline.apps.organizations.views import OrgView

urlpatterns = [
    url(r'^list/$', OrgView.as_view(), name="org_list"),
]
