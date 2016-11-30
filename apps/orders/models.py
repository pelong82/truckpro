from django.db import models
from apps.accounts.models import EmployeeUser


class Address(models.Model):
	city = models.CharField(max_length=60, default='Mexicali')
	state = models.CharField(max_length=60, default='Baja California')
	street = models.CharField(max_length=60)
	number = models.IntegerField()
	zip_code = models.IntegerField()


class Customer(models.Model):
	name = models.CharField(max_length=60, unique=True)
	address = models.OneToOneField(Address)
	phone = models.CharField(max_length=60, unique=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class Order(models.Model):
	employee = models.ForeignKey(EmployeeUser, blank=True)
	customer = models.ForeignKey(Customer)
	is_active = models.BooleanField(default=True)
	create = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return 'Order {}'.format(self.id)


class OrderItem(models.Model):
	order = models.ForeignKey(Order, related_name='items')
	measure = models.CharField(max_length=30)
	brand = models.CharField(max_length=40)
	serie = models.CharField(max_length=30)
	design = models.CharField(max_length=30)
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return '{}'.format(self.id)