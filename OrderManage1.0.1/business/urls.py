from django.urls import path,include
from business.views import login,manage,lookover,home


urlpatterns=[
    path('', login.login), #登录
    path('reg/',login.reg,name='check'), #登录
    path('home',home.home)
    path('managestaff',manage.staff), #管理员工
    path('managemenu',manage.menu),#管理菜单
    path('income',lookover.income),#查看收入情况
    path('analyze',lookover.analyze),#查看菜品销售分析
]

