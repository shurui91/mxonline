from django import forms
from captcha.fields import CaptchaField
from MxOnline.apps.users.models import UserProfile


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["nick_name", "gender", "birthday", "address"]


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["image"]


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=12)
    password = forms.CharField(required=True, max_length=20)


class DynamicLoginForm(forms.Form):
    captcha = CaptchaField()
