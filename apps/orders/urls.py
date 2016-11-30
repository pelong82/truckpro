from django.conf.urls import url
from apps.orders import views

urlpatterns = [
	url(r'^index/$', views.show, name='show'),
]
