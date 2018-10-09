from authapp.forms import ShopUserLoginForm


def include_login_form(request):
    form = ShopUserLoginForm()

    return {'login_form': form}
