from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from mainapp.models import ProductCategory, Product
from basketapp.models import Basket
from django.urls import reverse


def get_basket(request):
    if request.user.is_authenticated:
        return request.user.basket.all()
    else:
        return []


def index(request):
    context = {
        'page_title': 'главная',
        'basket': get_basket(request)
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    links_menu = ProductCategory.objects.all()
    products = Product.objects.all()

    context = {
        'page_title': 'каталог',
        'products': products,
        'links_menu': links_menu,
        'basket': get_basket(request),
    }
    return render(request, 'mainapp/products.html', context)


def category(request, pk):
    links_menu = ProductCategory.objects.all()

    if int(pk) == 0:
        category = {'name': 'все'}
        products = Product.objects.all().order_by('price')
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = category.product_set.order_by('price')

    context = {
        'title': 'продукты',
        'links_menu': links_menu,
        'category': category,
        'products': products,
        'basket': get_basket(request),
    }

    return render(request, 'mainapp/products_list.html', context)


def contact(request):
    locations = [
        {
            'city': 'Москва',
            'phone': '+7-888-888-8888',
            'email': 'info@geekshop.ru',
            'address': 'В пределах МКАД'
        },
        {
            'city': 'Санкт-Петербург',
            'phone': '+7-555-888-8888',
            'email': 'spb@geekshop.ru',
            'address': 'В пределах КАД'
        },
        {
            'city': 'Владивосток',
            'phone': '+7-333-888-8888',
            'email': 'fareast@geekshop.ru',
            'address': 'В пределах центра'
        },
    ]
    context = {
        'page_title': 'контакты',
        'locations': locations,
        'basket': get_basket(request),
    }
    return render(request, 'mainapp/contact.html', context)
