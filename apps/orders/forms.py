from django import forms
from django.forms.models import inlineformset_factory, BaseInlineFormSet, modelformset_factory
from apps.orders.models import Customer, Order, OrderItem


class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		exclude = ('created', 'modified',)
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'rfc': forms.TextInput(attrs={'class': 'form-control'}),
			'phone': forms.TextInput(attrs={'class': 'form-control'}),
			'state': forms.TextInput(attrs={'class': 'form-control'}),
			'city': forms.TextInput(attrs={'class': 'form-control'}),
			'colony': forms.TextInput(attrs={'class': 'form-control'}),
			'street': forms.TextInput(attrs={'class': 'form-control'}),
			'number': forms.TextInput(attrs={'class': 'form-control'}),
			'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
		}

		labels = {
			'name': 'Nombre:',
			'rfc': 'Rfc:',
			'phone': 'Teléfono',
			'state': 'Estado:',
			'city': 'Ciudad:',
			'colony': 'Colonia:',
			'street': 'Calle:',
			'number': 'Numero:',
			'zip_code': 'Código Postal',
		}


class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		exclude = ('created', 'modified', 'user', 'is_active')
		widgets = {
			'customer': forms.Select(attrs={'class': 'form-control', 'required': ''}),
		}

		labels = {
			'customer': 'Cliente:',
		}


class OrderItemForm(forms.ModelForm):
	class Meta:
		model = OrderItem
		exclude = ('order',)
		widgets = {
			'measure': forms.TextInput(attrs={'class': 'form-control', 'required': ''}),
			'brand': forms.TextInput(attrs={'class': 'form-control', 'required': ''}),
			'serie': forms.TextInput(attrs={'class': 'form-control', 'required': ''}),
			'design': forms.TextInput(attrs={'class': 'form-control', 'required': ''}),
			'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
		}

		labels = {
			'measure': 'Medida:',
			'brand': 'Marca:',
			'serie': 'Serie:',
			'design': 'Diseño:',
			'quantity': 'Cantidad:',
		}

OrderItemFormset = modelformset_factory(
	OrderItem,
	form=OrderItemForm,
)
OrderItemInlineFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm,
													formset=OrderItemFormset,
													extra=1, max_num=30, can_delete=True)
# OrderItemFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm,
# 													formset=BaseInlineFormSet,
# 													extra=1, max_num=30, can_delete=False)
OrderItemFormSetCreate = inlineformset_factory(Order, OrderItem, form=OrderItemForm,
													formset=BaseInlineFormSet,
													extra=1, max_num=30, can_delete=False)
