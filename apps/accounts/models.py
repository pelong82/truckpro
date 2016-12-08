from django.db import models
from django.conf import settings


# Create your models here.
class EmployeeUser(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
	job = models.CharField(max_length=40)

	def __str__(self):
		return '{}'.format(self.user.username)


class CustomerUser(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
	company = models.CharField(max_length=60)

	def __str__(self):
		return self.user.username
