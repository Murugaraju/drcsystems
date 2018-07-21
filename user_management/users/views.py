# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.


@login_required(login_url="login/")
def home(request):
    print "inside homeeeeee",request.method
    # if request.method == 'GET':
    #     form = LoginForm()
    #     print "form.is_valid()", form.is_valid()
    #     return render(request, "login.html", {'form': form})
    # else:
    #     form = LoginForm(request.POST)
    return render(request, "home.html")

# def register(request):
#     return render(request, "register.html")


def register(request):
    # print "inside register"

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            # username = userObj['username']
            email = userObj['email']
            password = userObj['password']
            # if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
            if not (User.objects.filter(email=email).exists()):
                User.objects.create_user(email, password)
                user = authenticate(email=email, password=password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')

    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})
