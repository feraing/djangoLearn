# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect


# Create your views here.
@login_required()
def index(request):
    return render(request, 'index.html')


def acc_login(request):
    login_err = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            login_err = "Wrong username or password!"

    return render(request, 'login.html', {'login_err': login_err})


@login_required()
def acc_logout(request):
    logout(request)
    return render(request, 'login.html')