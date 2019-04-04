from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from mainapp.models import Product
from basketapp.models import Basket

def index(request):
    pass


def add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
