from django.conf.urls import url
from django.contrib import admin
from palev import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rent/', views.rent, name='rent'),
    url(r'^clean/', views.clean, name='clean'),
    url(r'^chem/', views.chem, name='chem'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^admin/', admin.site.urls),
]
