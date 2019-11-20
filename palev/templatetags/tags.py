from django import template
from django.utils.safestring import mark_safe
from ..models import Page

register = template.Library()

@register.simple_tag
def header():
  header = Page.objects.get(page_link='<header>')
  return mark_safe(header.page_content)

@register.simple_tag
def footer():
  footer = Page.objects.get(page_link='<footer>')
  return mark_safe(footer.page_content)