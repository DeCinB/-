from django.urls import path,include
import views

urlpatterns=[
	path('menu/',views.get_menu),#菜单页面
	path('orderlist/',view.ordering,name='orderlist'),#下单结算页面 
	
]