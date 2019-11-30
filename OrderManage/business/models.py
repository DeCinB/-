from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class Cuisine(models.Model):


	name=models.CharField(primary_key=True,max_length=20,verbose_name='菜名')
	kind=models.ForeignKey('CuisineKind',to_field='kind',verbose_name='菜式',on_delete=models.CASCADE)
	price=models.DecimalField(max_digits=5,decimal_places=2,verbose_name='价格')
	#img=models.ImageField(verbose_name='图片',upload_to='')

	def __str__(self):
		return self.name

class CuisineKind(models.Model):
	"""docstring for CuisineKind"""
	kind=models.CharField(primary_key=True,max_length=20,verbose_name='菜式')
	num=models.IntegerField(verbose_name='数量')

	def __str__(self):
		return self.kind
		

class Desk(models.Model):

	desk_id=models.AutoField(primary_key=True,verbose_name='桌号')

	def __str__(self):
		return '桌'+str(self.desk_id)


class Order(models.Model):

	order_id=models.CharField(primary_key=True,max_length=20,verbose_name='订单号')
	desk_id=models.ForeignKey('Desk',to_field='desk_id',verbose_name='桌号',on_delete=models.CASCADE)
	time=models.DateTimeField(auto_now_add=True,verbose_name='下单时间')
	total_cost=models.DecimalField(max_digits=5,decimal_places=2,verbose_name='消费总额')

	def __str__(self):
		return self.order_id

class OrderDetail(models.Model):

	name=models.ForeignKey('Cuisine',to_field='name',verbose_name='菜名',on_delete=models.CASCADE)
	order_id=models.ForeignKey('Order',to_field='order_id',verbose_name='订单号',on_delete=models.CASCADE)
	num=models.IntegerField(verbose_name='数量',default=1)


	def __str__(self):
		return str(self.order_id)+str(self.name)

class Manager(models.Model):
	name=models.CharField(primary_key=True,max_length=20,verbose_name='登录名')
	pwd=models.CharField(verbose_name='密码',max_length=20)
	last_login=models.DateTimeField(verbose_name='最后登录时间',default=timezone.now)

	def __str__(self):
		return self.name