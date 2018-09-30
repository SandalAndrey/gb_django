from django.shortcuts import render
from productsapp.models import ProductCategory

def main(request):
    cats = ProductCategory.objects.all()

    return render(request, 'contactsapp/ext_contacts.html', {'categorys':cats})
