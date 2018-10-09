from django.contrib import auth
from django.shortcuts import HttpResponseRedirect, redirect
from django.urls import reverse

import json

from authapp.forms import ShopUserLoginForm

from django.contrib import messages


def login(request):
    login_form = ShopUserLoginForm(data=request.POST)

    if request.method == 'POST':
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                # return HttpResponseRedirect(reverse('/'))
                messages.success(request, 'Добро пожаловать на сайт')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
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
