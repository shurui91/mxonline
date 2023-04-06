from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=12)
    password = forms.CharField(required=True, max_length=20)
