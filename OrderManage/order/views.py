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



def ordering(request):

	return render(request,'order/success.html')