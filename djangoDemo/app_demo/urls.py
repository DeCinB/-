from django.urls import path,include
import app_demo.views as views

urlpatterns=[
	path('hello',views.hello),
	path('content',views.article_content),
	path('index',views.get_index_page),
	#path('detail',views.get_detail_page),
	path('detail/<int:article_id>',views.get_detail_page),
]