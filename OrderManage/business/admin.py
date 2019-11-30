from django.contrib import admin
from .models import Cuisine,CuisineKind,Desk,Order,OrderDetail,Manager

# Register your models here.
admin.site.register(Cuisine)
admin.site.register(CuisineKind)
admin.site.register(Desk)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Manager)
