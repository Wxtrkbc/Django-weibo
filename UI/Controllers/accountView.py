#!/usr/bin/env python
# coding=utf-8

from django.shortcuts import render,HttpResponse

def login(request):

    username = request.GET.get('username')
    password = request.GET.get('password')

    return HttpResponse('')