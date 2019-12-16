#manage模块, 管理菜单、员工
from django.shortcuts import render,redirect
from django.http import HttpResponse
from business.models import Manager
from django.http import JsonResponse
from OrderManage.settings import MEDIA_ROOT
import json
import time

def staff(request):
	#员工管理
	if request.method=="GET":
		allStaff=Manager.objects.all()

		return render(request,'business/manageStaff.html',{
					'allStaff':allStaff,
			})
	elif request.method=="POST":
		if request.POST['Name']:
			staffName=request.POST['Name']
			staff=Manager.objects.filter(name=staffName)
			if len(staff)>0:
				if request.POST.get('delete','off')=="on":
					staff[0].delete()
				else:
					if request.POST['Telephone']:
						staff[0].tel=request.POST['Telephone']
					if request.FILES.get('Photo','')!='':
						staffPho=request.FILES['Photo']
						fname='%s/staff/%s' % (MEDIA_ROOT,staffPho.name)
						with open(fname, 'wb') as pic:
							for c in staffPho.chunks():
								pic.write(c)
							staff[0].img='/staff/%s'%(staffPho.name)
					staff[0].save()
				
			else:
				staff=Manager(name=staffName)
				if request.POST.get('Telephone','')!='':
					staff.tel=request.POST['Telephone']
				if request.FILES.get('Photo','')!='':
					staffPho=request.FILES['Photo']
					fname='%s/staff/%s' % (MEDIA_ROOT,staffPho.name)
					with open(fname, 'wb') as pic:
						for c in staffPho.chunks():
							pic.write(c)
						staff.img='/staff/%s'%(staffPho.name)
				staff.save()

		return redirect("http://127.0.0.1:8000/business/managestaff")#重定向


def menu(request):
	#菜单管理
	return render(request,'business/manageMenu.html')

	
	