import random

from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from mainapp.models import ProductCategory, Product
from basketapp.models import Basket


def get_basket(request):
    if request.user.is_authenticated:
        return request.user.basket.all()
    else:
        return []


def get_hot_product():
    return random.choice(Product.objects.filter(is_active=True))


def get_same_products(hot_product):
    return hot_product.category.product_set.filter(is_active=True).exclude(pk=hot_product.pk)


def get_menu():
    return ProductCategory.objects.filter(is_active=True)


def index(request):
    context = {
        'page_title': 'главная',
        'basket': get_basket(request)
    }
    return render(request, 'mainapp/index.html', context)


def category(request, pk, page=1):
    if int(pk) == 0:
        category = {
            'pk': 0,
            'name': 'все',
        }
        products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = category.product_set.filter(is_active=True).order_by('price')

    paginator = Paginator(products, 2)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'title': 'продукты',
        'links_menu': get_menu(),
        'category': category,
        'products': products,
        'basket': get_basket(request),
    }

    return render(request, 'mainapp/products_list.html', context)


def products(request):
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    context = {
        'page_title': 'каталог',
        'links_menu': get_menu(),
        'basket': get_basket(request),
        'hot_product': hot_product,
        'same_products': same_products,
    }
    return render(request, 'mainapp/products.html', context)


def product(request, pk):
    context = {
        'title': 'продукт',
        'links_menu': get_menu(),
        'basket': get_basket(request),
        'object': get_object_or_404(Product, pk=pk),
    }
    return render(request, 'mainapp/product.html', context)


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
