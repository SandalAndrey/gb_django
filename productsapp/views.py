import json
import os

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Good, ProductCategory


def main(request):
    cat_id = request.GET.get('cat', '')
    if cat_id:
        goods = Good.objects.filter(category=cat_id)
    else:
        goods = Good.objects.all()

    print(cat_id)
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


# def category(request, cat_id=None):
#     cats = ProductCategory.objects.all()
#     goods = Good.objects.filter(category=cat_id)
#
#     return render(request, 'productsapp/ext_catalog.html', {'goods': goods, 'categorys': cats})


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
