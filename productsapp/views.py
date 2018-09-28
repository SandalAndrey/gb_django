from django.shortcuts import render, get_object_or_404
from .models import Good, ProductCategory
import json
from django.conf import settings
import os
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.template import loader


def main(request):
    goods = Good.objects.all()

    cats = ProductCategory.objects.all()

    if request.method == 'POST' and request.is_ajax():
        id = request.POST.get('id')
        if id:
            goods = goods.filter(category=id)
            # data = serializers.serialize('json', goods)
            # return HttpResponse(data, content_type="application/json")

            goods_html = loader.render_to_string('productsapp/goods.html', {'goods': goods}
                                                 )
            output_data = {'goods_html': goods_html}

            return JsonResponse(output_data)
    else:
        return render(request, 'productsapp/catalog.html', {'goods': goods, 'cats': cats})


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
