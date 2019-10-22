# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
  def __unicode__(self):
    return self.art_title

  art_title = models.CharField(max_length=100)
  art_text = models.TextField()
  published = models.BooleanField(blank=True, default=True)
