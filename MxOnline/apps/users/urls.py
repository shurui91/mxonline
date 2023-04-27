from django.urls import re_path as url
from MxOnline.apps.users.views import UserInfoView

urlpatterns = [
    url(r'^info/$', UserInfoView.as_view(), name="info"),
]
