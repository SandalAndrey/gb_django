from django.shortcuts import render, get_object_or_404
from .models import Good, ProductCategory
import json
from django.conf import settings
import os
from django.contrib.staticfiles.templatetags.staticfiles import static


def main(request, cat_id = None):
    goods = Good.objects.all()
    if cat_id:
        goods = goods.filter(category = cat_id)
    cats = ProductCategory.objects.all()

    return render(request, 'productsapp/catalog.html', {'goods': goods, 'cats':cats})


def good(request, good_id=1):
    good = get_object_or_404(Good, pk=good_id)

    characteristic = {}
    static_path = settings.STATICFILES_DIRS[0]

    with open(os.path.join(static_path, 'data.json'), encoding='utf-8') as f:
        characteristics = json.load(f)
    if characteristics and good_id < len(characteristics):
        characteristic = characteristics[good_id - 1]

    return render(request, 'productsapp/good.html', {'good': good, 'characteristics': characteristic})
