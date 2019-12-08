from django.shortcuts import render,redirect
from django.http import HttpResponse
from business.models import Manager
from django.contrib import messages

def login(request):
    return render(request,"business/login.html")

def reg(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        for people in Manager.objects.all().values_list('name','pwd'):
            if user_name == people[0] and password == people[1]:
                print(user_name,password)
                return redirect('http://127.0.0.1:8000/order/menu')#重定向
        #print(people[0],people[1])
        return render(request, 'business/error.html')

