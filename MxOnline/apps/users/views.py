from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        user_name = request.POST.get("username", "")
        password = request.POST.get("password", "")

        # 通过用户名密码查询用户是否存在
        # 1. 通过用户名查询到用户
        # 2. 需要先加密再通过加密之后的密码查询
        # user = UserProfile.objects.get(username=user_name, password=password)
        user = authenticate(username=user_name, password=password)
        # 登录成功之后redirect到主页
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {"msg": "用户名或密码错误"})
