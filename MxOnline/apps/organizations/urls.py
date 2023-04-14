from django.urls import re_path as url
from MxOnline.apps.organizations.views import OrgView

urlpatterns = [
    url(r'^list/$', OrgView.as_view(), name="list"),
    url(r'^add_ask/$', OrgView.as_view(), name="add_ask"),

]
