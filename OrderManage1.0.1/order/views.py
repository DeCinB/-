from django.shortcuts import render
from django.http import HttpResponse
from business.models import Cuisine,CuisineKind,Desk,Order,OrderDetail
from django.http import JsonResponse
import json
import time

# Create your views here.
def get_menu(request,d_id):
	if request.method=='GET':
	#获得菜品种类
		cuisine_kind=CuisineKind.objects.all()

		menu=Cuisine.objects.all()

		return render(request,'order/menu.html',
					{	
						'cuisine_kind':cuisine_kind,
						'menu':menu,
						'desk':d_id,
					}
				)
	elif request.method=="POST":
		if request.POST:
			if request.POST['desk_id']:
				deskId=request.POST['desk_id']
			if request.POST['total_cost']:
				total_cost=int(request.POST['total_cost'])
			if request.POST['customer_number']:
				customer_number=int(request.POST['customer_number'])
			if request.POST['note']:
				notes=request.POST['note']
			if request.POST['order_list']:
				order_list=json.loads(request.POST['order_list'])

			#生成订单
			d=Desk.objects.get(desk_id=deskId)
			orderTime=time.localtime();
			orderTime_str1=time.strftime("%y%m%d%H%M",orderTime)
			orderTime_str2=time.strftime("%X",orderTime);
			orderTime=time.strftime("%y%m%d%H%M",time.localtime());
			orderId=orderTime_str1+d.desk_id;
			order=Order(order_id=orderId,desk_id=d,total_cost=total_cost,customer_num=customer_number,note=notes)
			order.save()

			#生成订单内容
			allCuisines=Cuisine.objects.all()
			for cuisine in allCuisines:
				if str(cuisine.cuisine_id) in order_list:
					num=order_list[str(cuisine.cuisine_id)]
					orderDetail=OrderDetail(name=cuisine,order_id=order,num=num)
					orderDetail.save()

			return JsonResponse({"state":'success',"time":orderTime_str2,})
