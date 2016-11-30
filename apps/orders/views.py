from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import login, authenticate, logout
from apps.accounts.forms import LoginForm
from django.contrib.auth.models import User


def show(request):
	return render(request, 'orders/index.html', {})
