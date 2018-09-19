from django.shortcuts import render


def main(request):
    return render(request, 'productsapp/catalog.html')


def good(request, good_id=1):
    context = {'goodID': good_id}

    return render(request, 'productsapp/good.html', context=context)
