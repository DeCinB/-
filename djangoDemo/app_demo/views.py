from django.shortcuts import render#视图，与浏览器交互，模板
# Create your views here.
from django.http import HttpResponse
from app_demo.models import Article#引进模型
from django.core.paginator import Paginator#引进分页组件
'''

该模块定义了HttpResponese对象的API
HttpResponse属性：	
	content:返回内容，字符串类型
	charset:响应的编码字符集
	status_code：HTTP相应的状态码
'''

'''
hello时一个视图函数，每个视图函数必须第一个参数为request
request是django.http.HttpResponse的一个实例
'''

def hello(request):
	return HttpResponse('Hello World')


def article_content(request):
	article=Article.objects.all()[0]
	title=article.title
	brief_content=article.brief_content
	content=article.content
	article_id=article.article_id
	publish_date=article.publish_date

	return_str='title:%s\nbrief_content:%s\n'\
			   'content:%s\npublish_date:%s'%(title,
			   								  brief_content,
			   								  content,
			   								  publish_date)
	return HttpResponse(return_str)

def get_index_page(request):
	page=request.GET.get('page')
	if page:
		page=int(page)
	else:
		page=1


	all_article=Article.objects.all()
	top5_article_list=Article.objects.order_by('-publish_date')[:5]

	paginator=Paginator(all_article,3)
	page_num=paginator.num_pages

	page_article_list=paginator.page(page)

	if page_article_list.has_next():
		next_page=page+1
	else:
		next_page=page

	if page_article_list.has_previous():
		previous_page=page-1
	else:
		previous_page=page



	return render(request,'dynamic/index.html',
				 {
				 	'article_list':page_article_list,
				 	'page_num':range(1,page_num+1),
				 	'curr_page':page,
				 	'next_page':next_page,
				 	'previous_page':previous_page,
				 	'top5_article_list':top5_article_list
				 }
					)

def get_detail_page(request,article_id):
	all_article=Article.objects.all()
	curr_article=None
	previous_index=0
	next_index=0
	previous_article=None
	next_article=None

	for index,article in enumerate(all_article):
		if index==0:
			previous_index=0
			next_index=index+1
		elif index==len(all_article)-1:
			previous_index=index-1
			next_index=index
		else:
			previous_index=index-1
			next_index=index+1

		if article.article_id==article_id:
			curr_article=article
			previous_article=all_article[previous_index]
			next_article=all_article[next_index]
			break
			

	section_list=article.content.split('\n')
	#把文章
	return render(request,'dynamic/detail.html',
				 {
				 	'curr_article':article,
				 	'section_list':section_list,
				 	'previous_article':previous_article,
				 	'next_article':next_article,

				 }
					)