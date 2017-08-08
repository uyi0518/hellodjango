from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from polls import models   #from polls.models import sign 会报错，原因不明

def signon(request):
    return render(request,"polls/sign.html")
def signin(request):
    user1=request.POST.get("user",1)
    password1= request.POST.get("password", 1)
    email1= request.POST.get("email", 1)
    obj=models.sign(user=user1, password=password1,email=email1)
    obj.save()
    return HttpResponse("注册成功")
