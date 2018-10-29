import json
import os

from django.utils import timezone
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy

from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)

from productsapp.models import Good, ProductCategory
from productsapp.forms import (GoodModelForm, ProductCategoryModelForm)


class ProductListView(ListView):
    model = Good
    template_name = 'productsapp/ext_catalog.html'
    context_object_name = 'goods'
    paginate_by = 6
    cat_id = None

    def get_queryset(self):
        self.cat_id = self.request.GET.get('cat', '')
        if self.cat_id:
            self.goods = Good.objects.filter(category=self.cat_id)
        else:
            self.goods = Good.objects.all()
        return self.goods

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        cats = ProductCategory.objects.all()
        context['categorys'] = cats
        if self.cat_id:
            context['cat_id'] = self.cat_id

        return context


def main(request):
    cat_id = request.GET.get('cat', '')
    if cat_id:
        goods = Good.objects.filter(category=cat_id)
    else:
        goods = Good.objects.all()

    cats = ProductCategory.objects.all()

    # print(request, request.is_ajax())

    if request.method == 'POST' and request.is_ajax():
        id = request.POST.get('id')
        if id:
            goods = goods.filter(category=id)

            paginator = Paginator(goods, 6)

            page = request.POST.get('page')

            try:
                goods = paginator.page(page)
            except PageNotAnInteger:
                goods = paginator.page(1)
            except EmptyPage:
                goods = paginator.page(paginator.num_pages)

            # data = serializers.serialize('json', goods)
            # return HttpResponse(data, content_type="application/json")

            goods_html = loader.render_to_string('productsapp/inc_goods.html', {'goods': goods}
                                                 )
            output_data = {'goods_html': goods_html, 'cat_id': id}

            return JsonResponse(output_data)
    else:
        paginator = Paginator(goods, 6)

        page = request.GET.get('page')

        try:
            goods = paginator.page(page)
        except PageNotAnInteger:
            goods = paginator.page(1)
        except EmptyPage:
            goods = paginator.page(paginator.num_pages)

        context = {}
        context['goods'] = goods
        context['categorys'] = cats
        if cat_id:
            context['cat_id'] = cat_id

        return render(request, 'productsapp/ext_catalog.html', context=context)


class ProductDetailView(DetailView):
    model = Good
    template_name = 'productsapp/good.html'
    context_object_name = 'good'
    pk_url_kwarg = 'good_id'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)

        characteristic = {}
        static_path = settings.STATICFILES_DIRS[0]

        # Загрузка характеристик из файла.
        with open(os.path.join(static_path, 'data.json'), encoding='utf-8') as f:
            characteristics = json.load(f)
        if characteristics and self.kwargs['good_id'] < len(characteristics):
            characteristic = characteristics[self.kwargs['good_id'] - 1]

        context['characteristics'] = characteristic

        return context


class ProductCreateView(CreateView):
    model = Good
    template_name = 'productsapp/catalog_crud.html'
    context_object_name = 'form'
    form_class = GoodModelForm
    success_url = reverse_lazy('products:catalog')

    def form_valid(self, form):
        current_user = self.request.user
        if not current_user.is_anonymous:
            form.instance.author = current_user
            form.instance.published_date = timezone.now()
        return super(ProductCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['h1'] = 'Добавление товара'
        context['h2'] = 'Добавить товар'

        return context


class ProductUpdateView(UpdateView):
    model = Good
    template_name = 'productsapp/catalog_crud.html'
    form_class = GoodModelForm
    success_url = reverse_lazy('products:catalog')

    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['h1'] = 'Обновление товара'
        context['h2'] = 'Обновить товар'

        return context


class ProductDeleteView(DeleteView):
    model = Good
    template_name = 'productsapp/catalog_crud.html'
    success_url = reverse_lazy('products:catalog')

    def get_context_data(self, **kwargs):
        context = super(ProductDeleteView, self).get_context_data(**kwargs)
        context['h1'] = 'Удаление товара'
        context['h2'] = 'Удалить товар'

        return context
