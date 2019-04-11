from django.urls import path, re_path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    # re_path(r'^$', adminapp.index, name='index'),
    re_path(r'^$', adminapp.UsersListView.as_view(), name='index'),

    re_path(r'^shopuser/create/$', adminapp.shopuser_create, name='shopuser_create'),
    re_path(r'^shopuser/update/(?P<pk>\d+)/$', adminapp.shopuser_update, name='shopuser_update'),
    re_path(r'^shopuser/delete/(?P<pk>\d+)/$', adminapp.shopuser_delete, name='shopuser_delete'),

    re_path(r'^productcategories/$', adminapp.categories, name='categories'),
    re_path(r'^productcategory/create/$', adminapp.productcategory_create, name='productcategory_create'),
    re_path(r'^productcategory/update/(?P<pk>\d+)/$', adminapp.productcategory_update, name='productcategory_update'),
    re_path(r'^productcategory/delete/(?P<pk>\d+)/$', adminapp.productcategory_delete, name='productcategory_delete'),

    re_path(r'^products/(?P<pk>\d+)/$', adminapp.products, name='products'),
    re_path(r'^product/create/(?P<pk>\d+)/$', adminapp.product_create, name='product_create'),
    re_path(r'^product/read/(?P<pk>\d+)/$', adminapp.product_read, name='product_read'),
    re_path(r'^product/update/(?P<pk>\d+)/$', adminapp.product_update, name='product_update'),
    re_path(r'^product/delete/(?P<pk>\d+)/$', adminapp.product_delete, name='product_delete'),
]
