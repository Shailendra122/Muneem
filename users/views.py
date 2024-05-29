import django
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm

# Create your views here.

def register(request):
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your Account Has been created')
            return redirect('users/templates/core/base.html')
    else:
        form=UserRegistrationForm()
    context={'form':form}
    return render(request, 'users/register.html', context)

def logout(request):
    auth_logout(request)
    return redirect('home')
    