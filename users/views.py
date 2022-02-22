from django.shortcuts import render, redirect
from .models import WebUser
from django.contrib.auth import login
from django.http import HttpResponse


# Create your views here.


def register_make(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        if WebUser.objects.filter(email=email).exists() or WebUser.objects.filter(mobile=mobile) or WebUser.objects.filter(username=username).exists():
            return redirect('/WebUsers/error')
        new_user = WebUser(username=username, email=email, mobile=mobile, password=password)
        new_user.save()
        return redirect('/users/login')
    if request.method == "GET":
        return render(request, 'register.html')


def error(request):
    return render(request, 'error.html')


def User_login(request):
    if request == "GET":
        return render(request, '/users/login')
    else:
        password = request.POST.get("password")
        name = request.POST.get("username")
        filer = WebUser.objects.filter(username=name,password=password)
        if len(filer)>0:
            return render(request,"/admin")
        return HttpResponse("用户不存在")
