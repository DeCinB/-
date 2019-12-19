#商家首页
from django.shortcuts import render
from django.http import HttpResponse
from business.models import Order,OrderDetail
import json

def home(request):
	#获得主页
	if request.method == 'GET':
		all_order = Order.objects.all()
		unpaid_order =[]
		dish ={}
		for order in all_order:
			if not order.pay:
				unpaid_order.append(order)
				dish[order.order_id] = order.orderdetail_set.all()

		return render(request,'business/home.html',
					{
						'unpaid_list': unpaid_order,
						'dish_dict' : dish,
					})
	if request.method=='POST':
		if request.POST:
			if request.POST['order_id']:
				order_id = request.POST['order_id']
				desk = Order.objects.get(order_id=order_id)
				desk.pay = True
				desk.save()

		return HttpResponse(json.dumps({
			"status": 'success',
		}
		))


