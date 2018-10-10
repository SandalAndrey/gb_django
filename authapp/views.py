from django.contrib import auth
from django.shortcuts import HttpResponseRedirect, redirect, render
from django.urls import reverse

import json

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm

from django.contrib import messages


def do_login(request, name, password):
    user = auth.authenticate(username=name, password=password)
    if user and user.is_active:
        auth.login(request, user)
        # return HttpResponseRedirect(reverse('/'))
        messages.success(request, 'Добро пожаловать на сайт, {}'.format(user.first_name))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def login(request):
    login_form = ShopUserLoginForm(data=request.POST)

    if request.method == 'POST':
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            do_login(request, username, password)
        else:
            err_json = json.loads(login_form.errors.as_json())
            err = '; '.join(list(m['message'] for m in err_json['__all__']))

            messages.error(request, err)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    # content = {'title': title, 'login_form': login_form}
    # return HttpResponseRedirect(reverse('/'))
    return redirect('/')


def logout(request):
    auth.logout(request)
    # return HttpResponseRedirect(reverse('/'))
    return redirect('/')


def register(request):
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            # return HttpResponseRedirect(reverse('auth:login'))

            username = request.POST['username']
            password = request.POST['password1']

            do_login(request, username, password)

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        register_form = ShopUserRegisterForm()

    content = {'register_form': register_form}

    return render(request, 'authapp/ext_register.html', content)


def edit(request):
    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    content = {'edit_form': edit_form}

    return render(request, 'authapp/ext_edit.html', content)
