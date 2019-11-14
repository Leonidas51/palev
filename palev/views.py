# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Article, Page

def index(request):
  page = Page.objects.get(page_link='index')
  return render(request, 'page.html', {'page': page})

def rent(request):
  page = Page.objects.get(page_link='rent')
  return render(request, 'page.html', {'page': page})

def clean(request):
  page = Page.objects.get(page_link='clean')
  return render(request, 'page.html', {'page': page})

def chem(request):
  page = Page.objects.get(page_link='chem')
  return render(request, 'page.html', {'page': page})

def contact(request):
  page = Page.objects.get(page_link='contact')
  return render(request, 'page.html', {'page': page})

def carpets(request):
  page = Page.objects.get(page_link='carpets')
  return render(request, 'page.html', {'page': page})

def articles(request):
  article_list = Article.objects.filter(published=1).order_by('id')
  return render(request, 'articles.html', {'articles': article_list})

def article(request, pk):
  article = get_object_or_404(Article, pk=pk)
  return render(request, 'article.html', {'article': article})

def replacement(request):
  page = Page.objects.get(page_link='replacement')
  return render(request, 'page.html', {'page': page})

def cleaning(request):
  page = Page.objects.get(page_link='cleaning')
  return render(request, 'page.html', {'page': page})

def price(request):
  page = Page.objects.get(page_link='price')
  return render(request, 'page.html', {'page': page})

def unsorted_page(request, link):
  page = Page.objects.get(page_link=link)
  return render(request, 'page.html', {'page': page})

def send_carpet_form(request):
  if request.method == 'POST':
    count = 1
    message = ''

    while(request.POST.get(str(count) + '-size-w')):
      message += ('Тип: ' + request.POST.get(str(count) + '-type'))
      message += (', Размер: ' + request.POST.get(str(count) + '-size-w') + 'X' + request.POST.get(str(count) + '-size-h'))
      message += (', Количество: ' + request.POST.get(str(count) + '-amount'))
      message += '\n'

      count += 1

    message += ('\nДанные заказчика:\n')
    message += ('Имя: ' + request.POST.get('name') + ' Телефон: ' + request.POST.get('phone') + ' E-mail: ' + request.POST.get('email'))

    send_mail(
      u'Заказ грязезащитных ковров',
      message,
      'russian.memento@gmail.com',
      ['info@palev.ru']
    )

    return HttpResponse(
      json.dumps({'result': 'OK', 'message': message}),
      content_type="application/json"
    )
