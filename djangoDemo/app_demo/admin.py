from django.contrib import admin

# Register your models here.
#对应应用后台管理配置文件

from .models import Article

admin.site.register(Article)