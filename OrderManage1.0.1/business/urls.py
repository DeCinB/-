from django.urls import path,include
from business.views import login


urlpatterns=[
    path('', login.login), #?name来干嘛'''name='login'''
    path('reg/',login.reg,name='check'),

]

