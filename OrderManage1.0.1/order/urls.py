from django.urls import path,include
import order.views as views
from django.conf.urls import url

urlpatterns=[
	path('menu/<int:d_id>',views.get_menu),#菜单页面
	
]