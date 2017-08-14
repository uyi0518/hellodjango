from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import  ModelBackend
from  .models import  userProfile
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm,RegForm
from django.contrib.auth.hashers import make_password
from utilss.email_send import send_reg_email

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user=userProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e :
            return  None

class LoginView(View):
    def get(self,request):
        return render(request, "login/login.html", {})
    def post(self,request):
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return render(request, "index/index.html")
            else:
                return render(request, "login/login.html", {msg:"用户名或密码错误"})
        else:
            return render(request, "login/login.html", {login_form:login_form})

class RegView(View):
    def get(self,request):
        reg_form=RegForm()
        return  render(request, "login/reg.html",{'reg_form':reg_form})

    def post(self,request):
        reg_form = RegForm(request.POST)
        if  reg_form.is_valid():
            user_name = request.POST.get("email", "")
            pass_word = request.POST.get("password", "")
            user_Profile=userProfile()
            user_Profile.name=user_name
            user_Profile.email=user_name
            user_Profile.password=make_password(pass_word)
            user_Profile.save()
            send_reg_email(user_name,'register')
            pass
