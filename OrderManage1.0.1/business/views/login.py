from django.shortcuts import render,redirect
from django.http import HttpResponse
from business.models import Manager,Desk
from django.contrib import messages

def login(request):
    return render(request,"business/login.html")

def reg(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        d_id=request.POST.get('desk_id')
        desk=Desk.objects.filter(desk_id=d_id)
        for people in Manager.objects.all().values_list('name','pwd'):
            if user_name == people[0] and password == people[1] and len(desk)>0:
                return redirect("http://127.0.0.1:8000/order/menu/"+d_id)#重定向
        return render(request, 'business/error.html')
