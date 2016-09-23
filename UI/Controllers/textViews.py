#!/usr/bin/env python
# coding=utf-8
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render,HttpResponse

def test(request):
<<<<<<< HEAD
    return render(request, 'layout/_layout.html')

def personal(request):
    print(123)
    return render(request,'personal/personalpage.html')
=======
    return render(request, 'index/index.html')



def login(request):
    username = request.POST.get('username',None)
    pwd = request.POST.get('password',None)
    print(username, pwd)
    return render(request, 'layout/_layout.html')
>>>>>>> 123f7cceb5d034500f875b0e5b6510259e4b4b91
