from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

from adminapp.forms import ShopUserCreationAdminForm, ShopUserUpdateAdminForm, ProductCategoryEditForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory


@user_passes_test(lambda x: x.is_superuser)
def index(request):
    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser',
                                                 '-is_staff', 'username')
    context = {
        'title': 'админка/пользователи',
        'objects': users_list
    }

    return render(request, 'adminapp/index.html', context)


@user_passes_test(lambda x: x.is_superuser)
def categories(request):
    object_list = ProductCategory.objects.all().order_by('-is_active', 'name')
    context = {
        'title': 'админка/категории',
        'object_list': object_list
    }
    return render(request, 'adminapp/productcategory_list.html', context)


@user_passes_test(lambda x: x.is_superuser)
def products(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    object_list = category.product_set.all().order_by('name')
    context = {
        'title': 'админка/продукт',
        'category': category,
        'object_list': object_list,
    }
    return render(request, 'adminapp/product_list.html', context)


def shopuser_create(request):
    if request.method == 'POST':
        form = ShopUserCreationAdminForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:index'))
    else:
        form = ShopUserCreationAdminForm()
    context = {
        'title': 'пользователи/создание',
        'form': form
    }
    return render(request, 'adminapp/shopuser_update.html', context)


def shopuser_update(request, pk):
    current_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        form = ShopUserUpdateAdminForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:index'))
    else:
        form = ShopUserUpdateAdminForm(instance=current_user)
    context = {
        'title': 'пользователи/редактирование',
        'form': form
    }
    return render(request, 'adminapp/shopuser_update.html', context)


def shopuser_delete(request, pk):
    object = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        # user.delete()
        # вместо удаления лучше сделаем неактивным
        object.is_active = False
        object.save()
        return HttpResponseRedirect(reverse('myadmin:index'))
    context = {
        'title': 'пользователи/удаление',
        'user_to_delete': object
    }
    return render(request, 'adminapp/shopuser_delete.html', context)


def productcategory_update(request, pk):
    current_object = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        form = ProductCategoryEditForm(request.POST, request.FILES, instance=current_object)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:categories'))
    else:
        form = ProductCategoryEditForm(instance=current_object)
    context = {
        'title': 'категории/редактирование',
        'form': form
    }
    return render(request, 'adminapp/productcategory_update.html', context)
