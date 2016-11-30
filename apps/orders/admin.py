from django.contrib import admin
from .models import Address, Order, OrderItem, Customer


class OrderItemInline(admin.TabularInline):
	model = OrderItem


class OrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'customer', 'create']
	inlines = [OrderItemInline]

admin.site.register(Address)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Customer)