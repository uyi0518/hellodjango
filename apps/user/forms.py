from django import  forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username=forms.CharField(required=True)
    password=forms.CharField(required=True)

class RegForm(forms.Form):
    email=forms.CharField(required=True)
    password = forms.CharField(required=True)
    captcha = CaptchaField()