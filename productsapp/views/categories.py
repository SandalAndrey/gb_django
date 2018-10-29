from django.urls import reverse_lazy

from productsapp.models import ProductCategory
from productsapp.forms import (ProductCategoryModelForm)
from django.views.generic import (CreateView, UpdateView, DeleteView)


class CategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'productsapp/catalog_crud.html'
    form_class = ProductCategoryModelForm
    success_url = reverse_lazy('products:catalog')

    def get_context_data(self, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        context['h1'] = 'Добавление категории'
        context['h2'] = 'Добавить категорию'

        return context


class CategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'productsapp/catalog_crud.html'
    form_class = ProductCategoryModelForm
    success_url = reverse_lazy('products:catalog')

    def get_context_data(self, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        context['h1'] = 'Обновление категории'
        context['h2'] = 'Обновить категорию'

        return context


class CategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'productsapp/catalog_crud.html'
    success_url = reverse_lazy('products:catalog')

    def get_context_data(self, **kwargs):
        context = super(CategoryDeleteView, self).get_context_data(**kwargs)
        context['h1'] = 'Удаление категории'
        context['h2'] = 'Удалить категорию'

        return context
