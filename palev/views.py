# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Article

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

def carpets(request):
  return render(request, 'carpets.html')

def articles(request):
  article_list = Article.objects.filter(published=1).order_by('id')

  return render(request, 'articles.html', {'articles': article_list})

def article(request, pk):
  article = get_object_or_404(Article, pk=pk)

  return render(request, 'article.html', {'article': article})