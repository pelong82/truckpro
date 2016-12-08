from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.forms.formsets import formset_factory
from apps.accounts.forms import LoginForm
from apps.orders.forms import CustomerForm, OrderForm, OrderItemInlineFormSet
from apps.orders.forms import OrderItemFormSetCreate
from apps.orders.models import Customer
from apps.orders.models import Order, OrderItem


class MainPanelView(TemplateView):
	template_name = 'orders/index.html'


class CustomerListView(ListView):
	model = Customer
	template_name = 'orders/customer/list.html'

	def get_context_data(self, **kwargs):
		context = super(ListView, self).get_context_data(**kwargs)
		context['customers'] = Customer.objects.all().order_by('-created')[:6]
		return context


class CustomerCreateView(CreateView):
	form_class = CustomerForm
	template_name = 'orders/customer/create.html'
	success_url = reverse_lazy('orders:customer_list')


class CustomerEditView(UpdateView):
	model = Customer
	form_class = CustomerForm
	context_object_name = 'customer'
	template_name = 'orders/customer/edit.html'
	success_url = reverse_lazy('orders:customer_list')


class OrderListView(ListView):
	model = Order
	template_name = 'orders/order/list.html'

	def get_context_data(self, **kwargs):
		context = super(ListView, self).get_context_data(**kwargs)
		context['orders'] = Order.objects.all().order_by('-created')
		return context


class OrderCreateView(CreateView):
	form_class = OrderForm
	model = Order
	template_name = 'orders/order/create.html'
	success_url = reverse_lazy('orders:order_list')

	def get_context_data(self, **kwargs):
		context = super(OrderCreateView, self).get_context_data(**kwargs)
		if self.request.POST:
			context['formset'] = OrderItemFormSetCreate(self.request.POST, queryset=OrderItem.objects.none())
		else:
			context['formset'] = OrderItemFormSetCreate(queryset=OrderItem.objects.none())
		return context

	def form_valid(self, form):
		context = self.get_context_data()
		formset = context['formset']
		if len(formset) > 0:
			if formset.is_valid() and formset.is_valid():
				self.object = form.save(commit=False)
				self.object.user = self.request.user
				self.object.save()
				for f in formset:
					item = f.save(commit=False)
					item.order = self.object
					item.save()
				return HttpResponseRedirect(reverse_lazy('orders:order_list'))
		return HttpResponseRedirect(reverse_lazy('orders:order_create'))


def order_edit(request, pk):
	order = get_object_or_404(Order, pk=pk)
	form = OrderForm(instance=order)
	formset = OrderItemInlineFormSet(queryset=form.instance.orderitem_set.all())
	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		formset = OrderItemInlineFormSet(request.POST,
							queryset=form.instance.orderitem_set.all())
		if form.is_valid() and formset.is_valid():
			form.save()
			items = formset.save(commit=False)
			for item in formset.deleted_objects:
				item.delete()
			for item in items:
				item.order = order
				item.save()
			return HttpResponseRedirect(reverse_lazy('orders:order_list'))

	context = {
		'form': form,
		'formset': formset,
		'pk': pk
	}
	return render(request, 'orders/order/order_edit.html', context)


def customer_delete(request, id):
	Customer.objects.get(id=id).delete()
	return redirect('orders:customer_list')


def order_delete(request, pk):
	Order.objects.get(pk=pk).delete()
	return redirect('orders:order_list')


def index(request):
	return redirect(reverse_lazy('accounts:login'))
