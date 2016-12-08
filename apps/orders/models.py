from django.db import models
from django.contrib.auth.models import User
# from apps.accounts.models import EmployeeUser


class TimeStampModel(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)


class Customer(TimeStampModel):
	name = models.CharField(max_length=80, unique=True)
	rfc = models.CharField(max_length=15, unique=True)
	city = models.CharField(max_length=60, default='Mexicali')
	colony = models.CharField(max_length=60)
	state = models.CharField(max_length=60, default='Baja California')
	street = models.CharField(max_length=60)
	number = models.IntegerField()
	zip_code = models.IntegerField()
	phone = models.CharField(max_length=60, unique=True)

	def __str__(self):
		return self.name


class Order(TimeStampModel):
	user = models.ForeignKey(User)
	customer = models.ForeignKey(Customer)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return 'Order {}'.format(self.id)


class OrderItem(models.Model):
	order = models.ForeignKey(Order)
	measure = models.CharField(max_length=30)
	brand = models.CharField(max_length=40)
	serie = models.CharField(max_length=30)
	design = models.CharField(max_length=30)
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return '{}'.format(self.id)
