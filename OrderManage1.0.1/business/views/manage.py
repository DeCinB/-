#manage模块, 管理菜单、员工
from django.shortcuts import render
from django.http import HttpResponse
from business.models import Cuisine,CuisineKind,Desk,Order,OrderDetail
from django.http import JsonResponse
import json
import time

def staff(request):
	#员工管理
	return render(request,'business/manageStaff.html')
	



def menu(request):
	#菜单管理
	return render(request,'business/manageMenu.html')

	
	