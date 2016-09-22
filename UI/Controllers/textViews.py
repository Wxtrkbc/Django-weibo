#!/usr/bin/env python
# coding=utf-8

from django.shortcuts import render,HttpResponse

def test(request):
    return render(request, 'test.html')