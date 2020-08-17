# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from formapp import forms
from formapp.forms import myf
# Create your views here.

def index(request):
    myd = {"mytxt" : "this is Kartik..."}
    return render(request,'index1.html',context=myd)

def fm(request):
    form = forms.myf()

    if request.method == 'POST':

        form = forms.myf(request.POST)

        if form.is_valid():
            form.save()
            return index(request)
        else:
            print('Error...')    



    return render(request,'index2.html',{'form' : form})

