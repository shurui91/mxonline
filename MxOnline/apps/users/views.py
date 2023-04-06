from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

from MxOnline.apps.users.forms import LoginForm


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse("index"))


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        # 表单验证
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 通过用户名密码查询用户是否存在
            user_name = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            # 1. 通过用户名查询到用户
            # 2. 需要先加密再通过加密之后的密码查询
            # user = UserProfile.objects.get(username=user_name, password=password)
            user = authenticate(username=user_name, password=password)
            # 登录成功之后redirect到主页
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误", "login_form": login_form})

        else:
            return render(request, "login.html", {"login_form": login_form})
