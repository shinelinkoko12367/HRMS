from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import ListView
from django.contrib.auth import get_user_model


from django.urls import reverse_lazy
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.db.models import Q


from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
    
def logout_view(request):
	logout(request)
	return redirect('/')

def account_view(request):

	if not request.user.is_authenticated:
			return redirect("login")

	context = {}
	if request.POST:
		form = AccountUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.initial = {
					"email": request.POST['email'],
					"username": request.POST['username'],
			}
			form.save()
			context['success_message'] = "Updated"
	else:
		form = AccountUpdateForm(

			initial={
					"email": request.user.email, 
					"username": request.user.username,
				}
			)

	context['account_form'] = form

	return render(request, "account.html", context)


def home_view(request):
	return render(request, 'home.html', {})