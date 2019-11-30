from django.urls import path,include
import business.login as login

urlpatterns=[
    path('login/', login.login, name='login'),
    
]

