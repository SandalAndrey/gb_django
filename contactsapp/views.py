from django.shortcuts import render
from productsapp.models import ProductCategory
from .forms import MessageForm


def main(request):
    cats = ProductCategory.objects.all()
    form = MessageForm()

    return render(request, 'contactsapp/ext_contacts.html', {'categorys': cats, 'form': form})
