from django.contrib import admin
from .models import Order, OrderItem, Customer


class OrderItemInline(admin.TabularInline):
	model = OrderItem


class OrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'customer']
	inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Customer)
