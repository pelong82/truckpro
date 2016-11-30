from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import logout as logout_django

from apps.accounts.forms import LoginForm
from django.contrib.auth.models import User


def show(request):
	return HttpResponse('Hola')


def userLogin(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'],
							password=form.cleaned_data['password'])
			if user is not None:
				login(request, user)
				return redirect(reverse('orders:show'))
	form = LoginForm()
	context = {'form': form}
	return render(request, 'login.html', context)


def logout(request):
	logout_django(request)
	return redirect(reverse('accounts:login'))
