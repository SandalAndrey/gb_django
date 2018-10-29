from django import forms
from django.utils.translation import ugettext_lazy as _

from basketapp.models import (
    Basket
)


class BasketModelForm(forms.ModelForm):
    class Meta:
        model = Basket
        fields = ['product', 'quantity']

        labels = {
            'product': _('Товар'),
            'quantity': _('Количество'),
        }
