#!/usr/bin/env python
# coding=utf-8

from django.shortcuts import render, HttpResponse,redirect
from Service import UserService
import json
from django.contrib.auth.decorators import login_required
from Repository import UserRespository

from Repository import models


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        account_user_service = UserService.UserService(UserRespository.UserRespository())
        rep = account_user_service.login(request, username, password)
        return HttpResponse(json.dumps(rep))
    return render(request, 'layout/_layout.html')


def userProfile(request):
    uid = request.GET.get('uid')
    account_user_service = UserService.UserService(UserRespository.UserRespository())
    rep = account_user_service.fetch_all_by_uid(uid)
    return HttpResponse(json.dumps(rep))


# def index(request):
#     if not request.user.is_authenticated:
#         return redirect('/login/')
#     return render(request, 'index.html')

def index(request):
    return render(request, 'index/index.html')
