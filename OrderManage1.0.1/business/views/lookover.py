#查看收入情况、菜品销售分析
from django.shortcuts import render
from django.http import HttpResponse
from business.models import Cuisine,CuisineKind,Desk,Order,OrderDetail
from django.http import JsonResponse
import json
import time

def income(request):
	#查看收入
	return render(request,'business/income.html')
	

def analyze(request):
	#分析菜品销售情况
	return render(request,'business/analyze.html')
	
