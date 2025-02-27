from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your accout has been created you can now Log In')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
	if request.method == 'POST':
		u_from = UserUpdateForm(request.POST, instance=request.user)
		p_from = ProfileUpdateForm(request.POST,request.FILES ,instance=request.user.profile)

		if u_from.is_valid() and p_from.is_valid():
			u_from.save()
			p_from.save()
			messages.success(request, f'Your accout has been Updated')
			return redirect('profile')
	else:
		u_from = UserUpdateForm(instance=request.user)
		p_from = ProfileUpdateForm(instance=request.user.profile)


	context = {
		'u_from' : u_from,
		'p_from' : p_from,
	}

	return render(request, 'profile.html', context)