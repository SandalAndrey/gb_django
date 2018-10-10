from django.shortcuts import render, HttpResponseRedirect, render_to_response
from django.urls import reverse
from productsapp.models import ProductCategory
from contactsapp.forms import MessageForm
from django.contrib import messages


def main(request):
    cats = ProductCategory.objects.all()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            name = request.POST['name'] if request.POST['name'] else request.POST['username']
            messages.success(request, '{}, Ваше сообщение было успешно отправлено.'.format(name))

            return HttpResponseRedirect(reverse('contacts:main'))
        else:
            messages.success(request, 'Произошла ошибка при отправке сообщения.')
            return HttpResponseRedirect(reverse('contacts:main'))

    current_user = request.user
    initial = {}
    if not current_user.is_anonymous:
        initial['name'] = current_user.first_name
        initial['surname'] = current_user.last_name
        initial['email'] = current_user.email

    form = MessageForm(initial=initial)

    # return render_to_response(reverse('contacts:main'), {'categorys': cats, 'form': form})

    return render(request, 'contactsapp/ext_contacts.html', {'categorys': cats, 'form': form})
