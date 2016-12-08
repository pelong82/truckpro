from django.conf.urls import url
from apps.orders import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^panel/$', views.MainPanelView.as_view(), name='panel_index'),
	url(r'^panel/customers/list$', views.CustomerListView.as_view(), name='customer_list'),
	url(r'^panel/customers/create$', views.CustomerCreateView.as_view(), name='customer_create'),
	url(r'^panel/customers/edit/(?P<pk>\d+)$', views.CustomerEditView.as_view(), name='customer_edit'),
	url(r'^panel/customers/delete/(?P<id>\d+)$', views.customer_delete, name='customer_delete'),
	url(r'^panel/order/list$', views.OrderListView.as_view(), name='order_list'),
	url(r'^panel/order/create$', views.OrderCreateView.as_view(), name='order_create'),
	url(r'^panel/order/edit/(?P<pk>\d+)$', views.order_edit, name='order_edit'),
	url(r'^panel/order/delete/(?P<pk>\d+)$', views.order_delete, name='order_delete'),
]
