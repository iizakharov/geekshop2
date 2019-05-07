from django.urls import path, re_path
import ordersapp.views as ordersapp

app_name = 'ordersapp'

urlpatterns = [
    re_path(r'^$', ordersapp.OrderList.as_view(), name='index'),
    re_path(r'^order/create/$', ordersapp.OrderItemsCreate.as_view(), name='order_create'),

]
