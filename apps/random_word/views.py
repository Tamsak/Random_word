# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    return render(request, 'random_word/index.html')

def generate(request):
    request.session['counter'] +=1
    word = { 
        'random' : get_random_string(length=14)
    }
    return render(request, 'random_word/index.html',word)

def reset(request):
    if request.method == "POST":
        request.session['counter'] = 0
    return redirect('/random_word')