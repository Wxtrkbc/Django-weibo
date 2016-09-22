#!/usr/bin/env python
# coding=utf-8

from django.shortcuts import render, HttpResponse
from Service import UserService
import json
from Repository import UserRespository


def login(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    print(username, password)
    account_user_service = UserService.UserService(UserRespository.UserRespository())
    rep = account_user_service.login(request, username, password)

    return HttpResponse(json.dumps(rep))


def userProfile(request):
    uid = request.GET.get('uid')
    account_user_service = UserService.UserService(UserRespository.UserRespository())
    rep = account_user_service.fetch_all_by_uid(uid)
    return HttpResponse(json.dumps(rep))
