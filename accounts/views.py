from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import requests
from .forms import *


def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect ('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'] 
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        login(request, user)
        url = request.META.get('HTTP_REFERER')
        try:
            query=requests.utils.urlparse(url).query
            if query:
                params = dict(x.split('=') for x in query.split('&'))
                if 'next' in params:
                    nextPage = params['next']
                    messages.success(request, 'Welcome to Bellore Crafts')
                    return redirect (nextPage)
            else:
                messages.success(request, 'Welcome to Tirus & Esther Foundation')
                return redirect('dashboard')
        except:
            pass
            # return redirect('userprofile')
        
        else:
            messages.success(request, 'Username or Password is incorrect')

    return render (request, 'accounts/login_register.html')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
       
        if form.is_valid ():
            user = form.save(commit=False)
            user.first_name = user.email.split("@")[0]
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            
            return redirect('userprofile')
        
        else:
            messages.error(request, 'An error has occured during registration')


    context = {
        'page':page,
        'form':form
    }

    return render (request, 'accounts/login_register.html', context)

def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out')
    return redirect('login')