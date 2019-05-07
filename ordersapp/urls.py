from django.urls import path, re_path
import ordersapp.views as ordersapp

app_name = 'ordersapp'

urlpatterns = [
    re_path(r'^$', ordersapp.index, name='index'),

]
