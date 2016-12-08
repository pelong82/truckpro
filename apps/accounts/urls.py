from django.conf.urls import url
from apps.accounts import views

urlpatterns = [
	url(r'^show/$', views.show, name='show'),
	url(r'^login/$', views.userLogin, name='login'),
	url(r'^logout/$', views.logout, name='logout'),
	# url(r'^registrar/$', views.register, name='register'),
	url(r'^user/create/$', views.register, name='user_create'),
	url(r'^user/list/$', views.UserListView.as_view(), name='user_list'),
	url(r'^user/edit/(?P<pk>[0-9]+)$', views.UserUpdateView.as_view(), name='user_edit'),
	url(r'^user/delete/(?P<pk>[0-9]+)$', views.user_delete, name='user_delete'),
]
