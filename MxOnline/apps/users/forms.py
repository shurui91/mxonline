from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=12)
    password = forms.CharField(required=True, max_length=20)


class DynamicLoginForm(forms.Form):
    captcha = CaptchaField()
