from django.urls import path, re_path
import ordersapp.views as ordersapp

app_name = 'ordersapp'

urlpatterns = [
    re_path(r'^$', ordersapp.OrderList.as_view(), name='index'),
    re_path(r'^order/create/$', ordersapp.OrderItemsCreate.as_view(), name='order_create'),
    re_path(r'^order/read/(?P<pk>\d+)/$', ordersapp.OrderRead.as_view(), name='order_read'),
    re_path(r'^order/update/(?P<pk>\d+)/$', ordersapp.OrderItemsUpdate.as_view(), name='order_update'),
    re_path(r'^order/delete/(?P<pk>\d+)/$', ordersapp.OrderDelete.as_view(), name='order_delete'),

    re_path(r'^order/forming/complete/(?P<pk>\d+)/$', ordersapp.order_forming_complete, name='order_forming_complete'),

]
