#商家首页
from django.shortcuts import render
from django.http import HttpResponse
from business.models import Cuisine,CuisineKind,Desk,Order,OrderDetail
from django.http import JsonResponse
import json
import time

def home(request):
	#获得主页
	return render(request,'business/home.html')