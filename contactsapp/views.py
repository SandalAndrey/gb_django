from django.shortcuts import render, HttpResponseRedirect, render_to_response
from django.urls import reverse
from productsapp.models import ProductCategory
from contactsapp.forms import MessageForm


def main(request):
    cats = ProductCategory.objects.all()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('contacts:main'))

    form = MessageForm()

    # return render_to_response(reverse('contacts:main'), {'categorys': cats, 'form': form})

    return render(request, 'contactsapp/ext_contacts.html', {'categorys': cats, 'form': form})
