# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'signupform.html')

def signin(request):
    return render(request, 'signform.html')