from django.shortcuts import render, get_object_or_404

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


def index(request):
    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser',
                                                 '-is_staff', 'username')
    context = {
        'title': 'админка/пользователи',
        'objects': users_list
    }

    return render(request, 'adminapp/index.html', context)


def categories(request):
    object_list = ProductCategory.objects.all()
    context = {
        'title': 'админка/категории',
        'object_list': object_list
    }
    return render(request, 'adminapp/productcategory_list.html', context)


def products(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    object_list = category.product_set.all().order_by('name')
    context = {
        'title': 'админка/продукт',
        'category': category,
        'object_list': object_list,
    }
    return render(request, 'adminapp/product_list.html', context)
