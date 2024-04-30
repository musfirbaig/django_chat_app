from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SignupUser, LoginForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def frontpage(request):
    return render(request, 'core/landing_page.html')

def signuppage(request):
    if request.method == 'POST':
        form = SignupUser(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            return redirect(reverse('core:frontpage'))
    
    form = SignupUser()
    return render(request, 'core/signup_page.html', {'form': form})

def loginpage(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('core:frontpage'))
    else: 
        form = LoginForm()

        return render(request, 'core/login_page.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect(reverse('core:frontpage'))
