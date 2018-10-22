from django import forms
from django.utils.translation import ugettext_lazy as _

from productsapp.models import (
    ProductCategory, Good
)


class ProductCategoryModelForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name', 'description']
        labels = {
            'name': _('Название'),
            'description': _('Описание'),
        }


class GoodModelForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = [
            'category', 'name', 'photos', 'short_desc', 'description', 'price'
        ]
