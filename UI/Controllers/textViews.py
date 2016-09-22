#!/usr/bin/env python
# coding=utf-8
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render,HttpResponse

def test(request):
    return render(request, 'layout/_layout.html')



def login(request):
    username = request.POST.get('username',None)
    pwd = request.POST.get('password',None)
    print(username, pwd)
    return render(request, 'layout/_layout.html')