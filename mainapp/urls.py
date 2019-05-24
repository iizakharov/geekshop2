from django.urls import path, re_path
from django.views.decorators.cache import cache_page

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', mainapp.index, name='index'),
    re_path(r'^category/(?P<pk>\d+)/(?P<page>\d+)/ajax/$', cache_page(3600)(mainapp.category), name='category'),
    # re_path(r'^category/(?P<pk>\d+)/(?P<page>\d+)/ajax/$', mainapp.category, name='category'),
    re_path(r'^category/(?P<pk>\d+)/(?P<page>\d+)/$', mainapp.category, name='category'),
    # path('<int:pk>/', mainapp.category, name='category'),
    re_path(r'^products/$', mainapp.products, name='products'),
    re_path(r'^product/(?P<pk>\d+)/$', mainapp.product, name='product'),

    re_path(r'^contact/$', mainapp.contact, name='contact'),
]
