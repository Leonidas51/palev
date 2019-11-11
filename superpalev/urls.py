from django.conf.urls import url
from django.contrib import admin
from palev import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rent/', views.rent, name='rent'),
    url(r'^clean/', views.clean, name='clean'),
    url(r'^chem/', views.chem, name='chem'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^carpets/', views.carpets, name='carpets'),
    url(r'^articles/', views.articles, name='articles'),
    url(r'^article/(?P<pk>[0-9]+)$', views.article, name='article'),
    url(r'^replacement/', views.replacement, name='replacement'),
    url(r'^cleaning/', views.cleaning, name='cleaning'),
    url(r'^send_carpet_form/$', views.send_carpet_form, name='send_carpet_form'),
    url(r'^admin/', admin.site.urls),
]
