from django.shortcuts import render
from django.http import HttpResponse
from business.models import Manager
from django.contrib import messages

def login(request):
    return render(request,"login.html")

def reg(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        for people in Manager.objects.all().values_list('name','pwd'):
            if user_name == people[0] and password == people[1]:
                print(user_name,password)
                return render(request, 'success.html')
            else:
                print(people[0],people[1])
                return render(request, 'error.html')

