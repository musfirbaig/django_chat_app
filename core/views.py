from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SignupUser

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