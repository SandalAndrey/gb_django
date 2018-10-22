import json
import os

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy

from .models import Good, ProductCategory
from productsapp.forms import (GoodModelForm, ProductCategoryModelForm)


def main(request):
    cat_id = request.GET.get('cat', '')
    if cat_id:
        goods = Good.objects.filter(category=cat_id)
    else:
        goods = Good.objects.all()

    cats = ProductCategory.objects.all()

    # print(request, request.is_ajax())

    if request.method == 'POST' and request.is_ajax():
        id = request.POST.get('id')
        if id:
            goods = goods.filter(category=id)

            paginator = Paginator(goods, 6)

            page = request.POST.get('page')

            try:
                goods = paginator.page(page)
            except PageNotAnInteger:
                goods = paginator.page(1)
            except EmptyPage:
                goods = paginator.page(paginator.num_pages)

            # data = serializers.serialize('json', goods)
            # return HttpResponse(data, content_type="application/json")

            goods_html = loader.render_to_string('productsapp/inc_goods.html', {'goods': goods}
                                                 )
            output_data = {'goods_html': goods_html, 'cat_id': id}

            return JsonResponse(output_data)
    else:
        paginator = Paginator(goods, 6)

        page = request.GET.get('page')

        try:
            goods = paginator.page(page)
        except PageNotAnInteger:
            goods = paginator.page(1)
        except EmptyPage:
            goods = paginator.page(paginator.num_pages)

        context = {}
        context['goods'] = goods
        context['categorys'] = cats
        if cat_id:
            context['cat_id'] = cat_id

        return render(request, 'productsapp/ext_catalog.html', context=context)


def good(request, good_id=1):
    good = get_object_or_404(Good, pk=good_id)

    characteristic = {}
    static_path = settings.STATICFILES_DIRS[0]

    # Загрузка характеристик из файла.
    with open(os.path.join(static_path, 'data.json'), encoding='utf-8') as f:
        characteristics = json.load(f)
    if characteristics and good_id < len(characteristics):
        characteristic = characteristics[good_id - 1]

    return render(request, 'productsapp/good.html', {'good': good, 'characteristics': characteristic})


def product_create(request):
    template_name = 'productsapp/catalog_crud.html'
    success_url = reverse_lazy('products:catalog')
    form = GoodModelForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            current_user = request.user
            if not current_user.is_anonymous:
                new_good = form.save(commit=False)
                new_good.author = current_user
                new_good.publish()
                # form.save()

                return redirect(success_url)

    return render(request, template_name, {'form': form, 'h1': 'Добавление товара', 'h2': 'Добавить товар'})


def product_update(request, pk):
    template_name = 'productsapp/catalog_crud.html'
    success_url = reverse_lazy('products:catalog')
    obj = get_object_or_404(Good, pk=pk)

    form = GoodModelForm(instance=obj)

    if request.method == 'POST':
        form = GoodModelForm(
            request.POST,
            instance=obj
        )

        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(request, template_name, {'form': form, 'h1': 'Обновление товара', 'h2': 'Обновить товар '})


def product_delete(request, pk):
    template_name = 'productsapp/catalog_crud.html'
    success_url = reverse_lazy('products:catalog')
    obj = get_object_or_404(Good, pk=pk)

    if request.method == 'POST':
        obj.delete()

        return redirect(success_url)

    return render(request, template_name, {'h1': 'Удаление товара', 'h2': 'Удалить товар ' + obj.name})


def category_create(request):
    template_name = 'productsapp/catalog_crud.html'
    success_url = reverse_lazy('products:catalog')
    form = ProductCategoryModelForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

        return redirect(success_url)

    return render(request, template_name, {'form': form, 'h1': 'Добавление категории', 'h2': 'Добавить категорию'})


def category_update(request, pk):
    template_name = 'productsapp/catalog_crud.html'
    success_url = reverse_lazy('products:catalog')
    obj = get_object_or_404(ProductCategory, pk=pk)

    form = ProductCategoryModelForm(instance=obj)

    if request.method == 'POST':
        form = ProductCategoryModelForm(
            request.POST,
            instance=obj
        )

        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(request, template_name, {'form': form, 'h1': 'Обновление категории', 'h2': 'Обновить категорию '})


def category_delete(request, pk):
    template_name = 'productsapp/catalog_crud.html'
    success_url = reverse_lazy('products:catalog')
    obj = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        obj.delete()

        return redirect(success_url)

    return render(request, template_name, {'h1': 'Удаление категории', 'h2': 'Удалить категорию ' + obj.name})
