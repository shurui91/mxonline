from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

from MxOnline.apps.users.forms import LoginForm, DynamicLoginForm, UploadImageForm


class UserInfoView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request, *args, **kwargs):
        return render(request, "usercenter-info.html")


class UploadImageView(LoginRequiredMixin, View):
    login_url = "/login/"

    # def save_file(self, file):
    #     with open("C:/Users/Administrator/PycharmProjects/MxOnline/media/head_image/uploaded.jpg", "wb") as f:
    #         for chunk in file.chunks():
    #             f.write(chunk)

    def post(self, request, *args, **kwargs):
        # 处理用户上传的头像
        image_form = UploadImageForm(request.POST, request.FILES, instance=request.user)
        if image_form.is_valid():
            image_form.save()
            return JsonResponse({
                "status": "success"
            })
        else:
            return JsonResponse({
                "status": "fail"
            })
        # files = request.FILES["image"]
        # self.save_file(files)

        # 1. 如果同一个文件上传多次，相同名称的文件应该如何处理
        # 2. 文件的保存路径应该写入到user
        # 3. 还没有做表单验证


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse("index"))


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # 如果登陆成功，去主页
            return HttpResponseRedirect(reverse("index"))

        login_form = DynamicLoginForm()
        next = request.GET.get("next", "")
        return render(request, "login.html", {
            "login_form": login_form,
            "next": next,
        })

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
            # 登录成功之后redirect到登录前的页面
            if user is not None:
                login(request, user)
                # 在登陆成功后，虽然账号密码对，但是网页url不变，所以不能直接用render
                # return render(request, "index.html")
                next = request.GET.get("next", "")
                if next:
                    return HttpResponseRedirect(next)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误", "login_form": login_form})

        else:
            return render(request, "login.html", {"login_form": login_form})
