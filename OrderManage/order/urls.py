from django.urls import path,include
import order.views as views
from django.conf.urls import url

urlpatterns=[
	path('menu/',views.get_menu),#菜单页面
	path('orderlist/',views.ordering,name='orderlist'),#下单结算页面 
]