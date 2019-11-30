from django.db import models

# Create your models here.
class Cuisine(models.Model):
	id=models.AutoField(primary_key=True,verbose_name='产品序号')
	kind=models.ForeignKey('CuisineKind',to_field='id')
	name=models.CharField(verbose_name='菜名')
	price=models.FloatField(max_digits=5,decimal_places=2,verbose_name='价格')
	img=models.ImageField(verbose_name='图片')

	def __str__(self):
		return self.name

class CuisineKind(models.Model):
	"""docstring for CuisineKind"""

	def __str__(self):
		return self.
		

class Desk(models.Model):

	def __str__(self):
		return self.


class Order(models.Model):

	def __str__(self):
		return self.

class OrderDetail(models.Model):

	def __str__(self):
		return self.

class Manager(models.Model):

	def __str__(self):
		return self.