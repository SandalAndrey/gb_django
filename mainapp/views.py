from django.shortcuts import render
from productsapp.models import ProductCategory, Good


def main(request):
    cats = ProductCategory.objects.all()
    goods = []
    for cat in cats:
        goods.append(Good.objects.filter(category=cat.pk)[0])
    return render(request, 'mainapp/index.html', {'goods': goods})
