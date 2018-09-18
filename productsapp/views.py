from django.shortcuts import render


def main(request):
    return render(request, 'productsapp/catalog.html')

def good(request):
    context={'goodID':request.path_info.split('/')[2]}
    print(request.path_info.split('/')[2])
    return render(request, 'productsapp/good.html', context=context)
