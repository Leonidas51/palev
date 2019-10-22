# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
  return render(request, 'index.html')

def rent(request):
  return render(request, 'rent.html')

def clean(request):
  return render(request, 'clean.html')

def chem(request):
  return render(request, 'chem.html')

def contact(request):
  return render(request, 'contact.html')