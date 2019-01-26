from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import json
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UserForm


def user_login(request):
    if request.user.is_authenticated:
        return HttpResponse('Already Logged in ')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username = username, password = password)
                if user is not None:
                    login(request,user)
                    return HttpResponse('You are now logged in')
                else:
                    messages.error(request,'Username or Password is not correct.')
                    return HttpResponseRedirect('/')           
        else:
            form = LoginForm()
            return render (request, 'home/index.html',{'form':form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            return HttpResponseRedirect('/')
        else:
            messages.error(request,"Some Error On the Form.")
            return HttpResponse(request,'user/student_form.html')
    else:
        user_form = UserForm()
        return render(request, 'users/sign_up.html', { 'user_form':user_form})
