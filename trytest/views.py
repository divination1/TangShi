from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from trytest.models import User


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def sign(request):
    if request.method == "POST":
        data_get = request.POST
    elif request.method == "GET":
        data_get = request.GET
    else:
        return JsonResponse({"success": 0, "msg": "sign failed"})

    phonenumber = data_get.get("phonenumber")
    studentnumber = data_get.get("studentnumber")
    password = data_get.get("password")
    try:
        this_user = User.objects.get(PhoneNumber=phonenumber)
    except:
        return JsonResponse({"status": -1, "msg": "user doesn't exist", "phonenumber":phonenumber})
    if this_user.Password == password:
        print("2233")
        return JsonResponse({"status": 1, "msg": "登录成功", "data":"true"})
    else:
        return JsonResponse({"status": 0, "msg": "登录失败"})


def register(request):
    if request.method == "POST":
        data_get = request.POST
    elif request.method == "GET":
        data_get = request.GET
    else:
        return JsonResponse({"success": 0, "msg": "register failed"})

    username = data_get.get("username")
    phonenumber = data_get.get("phonenumber")
    studentnumber = data_get.get("studentnumber")
    password = data_get.get("password")

    this_user = User(UserName=username, Password=password, StudentNumber=studentnumber, PhoneNumber=phonenumber)
    try:
        User.objects.get(UserName=username)
        return JsonResponse({"status": -1, "msg": "user name exists"})
    except:
        try:
            User.objects.get(StudentNumber=studentnumber)
            return JsonResponse({"status": -1, "msg": "student has already register"})
        except:
            try:
                User.objects.get(PhoneNumber=phonenumber)
                return JsonResponse({"status": -1, "msg": "phone user has register"})
            except:
                this_user.save()
                return JsonResponse({"status": 1, "msg": "注册成功"})
