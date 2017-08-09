from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import  ModelBackend
from  .models import  userProfile
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user=userProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e :
            return  None

class LoginView(View):
    def get(self,requset):
        return render(request, "login/sign.html", {})
    def post(self,requset):
        login_form=LoginForm(requset.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return render(request, "index/index.html")
            else:
                return render(request, "login/sign.html", {msg:"用户名或密码错误"})



