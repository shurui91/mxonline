"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from django.views.generic import TemplateView

from MxOnline.apps.users.views import LoginView, LogoutView
from MxOnline.apps.organizations.views import OrgView
from MxOnline.settings import MEDIA_ROOT
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    url(r'^captcha/', include('captcha.urls')),

    # 配置上传文件的访问url，没有这一行代码，media文件无法正常显示
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', serve, {"document_root":STATIC_ROOT}),
    url(r'^org_list/', OrgView.as_view(), name="org_list"),

    # 机构相关页面
    url(r'^org/', include(('MxOnline.apps.organizations.urls', "organizations"), namespace='org')),

    # 用户相关操作
    url(r'^op/', include(('MxOnline.apps.operations.urls', "operations"), namespace='op')),

    # 机构相关页面
    url(r'^course/', include(('MxOnline.apps.courses.urls', "courses"), namespace='course')),
]
