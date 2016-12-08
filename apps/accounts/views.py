from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import logout as logout_django

from django.views.generic import ListView, UpdateView

from apps.accounts.forms import LoginForm, UserRegistrationForm, UserUpdateForm
from django.contrib.auth.models import User


class UserListView(ListView):
	model = User
	template_name = 'user/user_list.html'

	def get_context_data(self, **kwargs):
		context = super(UserListView, self).get_context_data(**kwargs)
		context['users'] = User.objects.all()
		return context


class UserUpdateView(UpdateView):
	model = User
	context_object_name = 'usuario'
	template_name = 'user/user_edit.html'
	form_class = UserUpdateForm
	success_url = reverse_lazy('accounts:user_list')

	def get_object(self, *args, **kwargs):
		user = get_object_or_404(User, pk=self.kwargs['pk'])
		return user

# def user_edit(request, pk):
# 	user = User.objects.get(pk=pk)
# 	print('El usuario es ', user.username)
# 	if request.method == 'POST':
# 		form = UserUpdateForm(request.POST, instance=user)
# 		if form.is_valid():
# 			print("datos correctos")
# 	form = UserUpdateForm(instance=user)
# 	return render(request, 'user/user_edit.html', {'form': form, 'usuario': user.id})


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
				return redirect(reverse('orders:panel_index'))
	form = LoginForm()
	context = {'form': form}
	return render(request, 'login.html', context)


def user_delete(request, pk):
	user = get_object_or_404(User, pk=pk)
	user.delete()
	return redirect('accounts:user_list')


def logout(request):
	logout_django(request)
	return redirect(reverse('accounts:login'))


def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.set_password(
				form.cleaned_data['password'])
			new_user.save()
			return redirect(reverse_lazy('accounts:user_list'))
	form = UserRegistrationForm()
	return render(request, 'user/user_create.html', {'form': form})

