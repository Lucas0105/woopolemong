from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

from accounts.forms import CustomUserCreationForm

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('portfolios:index')
    elif request.method == 'GET':
        form = AuthenticationForm()
    
    context = {
        'form' : form,
    }

    return render(request, 'accounts/login.html', context)


def logout():
    pass

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()

    context = {
        'form' : form,
    }

    return render(request, 'accounts/signup.html', context)


def signout():
    pass

def findpassword():
    pass
