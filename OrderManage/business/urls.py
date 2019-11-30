from django.urls import path,include
import views

urlpatterns=[
	#收银
    url(r'^home/$', home.get_index, name='home'),
    url(r'^pay/$', home.ge_tpay, name='pay'),
    url(r'^historyorder', get_history_orders.paging, name='historyorder'),

#管理  
    # 菜的管理
    url(r'^managecuisine/$', manage_menu.get_managecuisine, name='manage_cuisine'),
    # 菜单管理
    url(r'^managemenu/$', manage_menu.get_index, name='manage_menu'),
#收入
    url(r'^incomeday/$', income.day, name='income_day'),
    url(r'^incomemonth/$', income.month, name='income_month'),
    url(r'^incomeyear/$', income.year, name='income_year'),
#分析
    url(r'^analyze/$', analyze.get_index, name='analyze'),

#登陆
    url(r'^login/$', login.login, name='login'),
    url(r'^logout/$', login.logout, name='logout'),
]

