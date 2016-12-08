from django import forms
from django.contrib.auth.models import User
from apps.accounts.models import EmployeeUser


class LoginForm(forms.Form):
	username = forms.CharField(max_length=30,
		widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
	password = forms.CharField(max_length=20,
		widget=forms.PasswordInput(attrs={'placeholder': 'Constraseña'}))


class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Password',
								widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(label='Confirmar Password',
								widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	username = forms.CharField(max_length=30,
								widget=forms.TextInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(max_length=60, label='Nombre:',
								widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=60, label='Apellido:',
								widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.CharField(max_length=40,
								widget=forms.EmailInput(attrs={'class': 'form-control'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

		labels = {
			'first_name': 'Nombre:'
		}

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError("Los Password no son iguales")
		return cd['password2']

	def clean_email(self):
		cd = self.cleaned_data
		try:
			User.objects.get(email=cd['email'])
			raise forms.ValidationError('El email ya esta en uso')
		except User.DoesNotExist:
			return cd['email']


class UserUpdateForm(forms.ModelForm):
	username = forms.CharField(max_length=30,
								widget=forms.TextInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(max_length=60, label='Nombre:',
								widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=60, label='Apellido:',
								widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.CharField(max_length=40,
								widget=forms.EmailInput(attrs={'class': 'form-control'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email=email).exclude(pk=self.instance.id).count():
			raise forms.ValidationError('El email ya esta en uso')
		return email
