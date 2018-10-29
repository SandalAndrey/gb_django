from basketapp.forms import BasketModelForm
from basketapp.models import Basket
from django.db.models import Sum


def include_basket(request):
    basket=[]
    total_price = 0
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        for item in basket:
            total_price+=item.product.price*item.quantity

    print(basket)
    return {'basket': basket, 'total':total_price}