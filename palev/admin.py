# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Article, Page

class ArticleAdmin(admin.ModelAdmin):
  readonly_fields = ('id',)

class PageAdmin(admin.ModelAdmin):
  readonly_fields = ('id',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Page, PageAdmin)
