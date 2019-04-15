from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from mainapp.models import Product
from basketapp.models import Basket
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from django.template.loader import render_to_string
from django.http import JsonResponse


@login_required
def index(request):
    basket_items = request.user.basket.order_by('product__category')

    context = {
        'title': 'корзина',
        'basket_items': basket_items,
    }
    return render(request, 'basketapp/index.html', context)


@login_required
def add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('main:product',
                                            kwargs={
                                                'pk': pk,
                                            }))

    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def remove(request, pk):
    get_object_or_404(Basket, pk=pk).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def update(request, pk, quantity):
    if request.is_ajax():
        basket_item = get_object_or_404(Basket, pk=int(pk))
        quantity = int(quantity)
        if quantity > 0:
            basket_item.quantity = quantity
            basket_item.save()
        else:
            basket_item.delete()

        context = {
            'basket_items': request.user.basket.all().order_by('product__category'),
        }
        result = render_to_string('basketapp/includes/inc__basket_list.html', context)

        return JsonResponse({
            'result': result
        })
