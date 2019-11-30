from django.shortcuts import render
from django.http import HttpResponse
from business.models import Cuisine,CuisineKind,Desk

# Create your views here.
def get_menu(request):


	return render(request,'order/menu.html',
					{	
						'cuisine_kind':cuisine_kind,
						'cuisine_list':cuisine_list,
						'hotdishes_list':hotdishes_list
					}
				)


def order_list(request):


	return render(request,'order/order_list.html',
					{	
						'choose_list':choose_list,
						'total_price':total_price,
					}
				)


def order_action(request):

	return render(request,'order/success.html')