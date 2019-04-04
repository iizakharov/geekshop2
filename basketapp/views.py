from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from mainapp.models import Product
from basketapp.models import Basket


def index(request):
    basket_items = request.user.basket.order_by('product__category')

    context = {
        'title': 'корзина',
        'basket_items': basket_items,
    }
    return render(request, 'basketapp/index.html', context)


def add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove(request, pk):
    get_object_or_404(Basket, pk=pk).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
