from django.conf.urls import url
from apps.accounts import views

urlpatterns = [
	url(r'^show/$', views.show, name='show'),
	url(r'^login/$', views.userLogin, name='login'),
	url(r'^logout/$', views.logout, name='logout'),
]
