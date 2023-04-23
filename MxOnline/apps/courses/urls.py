from django.urls import path
from django.urls import re_path as url

from MxOnline.apps.courses.views import CourseListView

urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name="list"),
]
