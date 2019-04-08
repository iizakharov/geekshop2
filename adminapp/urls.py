from django.urls import path, re_path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    re_path(r'^$', adminapp.index, name='index'),
    re_path(r'^categories/$', adminapp.categories, name='categories'),
    re_path(r'^products/(?P<pk>\d+)/$', adminapp.products, name='products'),
]
