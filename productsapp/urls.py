from django.urls import path, re_path
from productsapp.views import (main, ProductDetailView, ProductCreateView, ProductDeleteView, ProductUpdateView,
                               ProductListView, CategoryUpdateView, CategoryCreateView, CategoryDeleteView)

app_name = 'products'

urlpatterns = [
    re_path(r'^$', ProductListView.as_view(), name='catalog'),
    path('<int:good_id>/', ProductDetailView.as_view(), name='detail'),
    path('create_prod/', ProductCreateView.as_view(), name='create_prod'),
    path('update_prod/<int:pk>/', ProductUpdateView.as_view(), name='update_prod'),
    path('delete_prod/<int:pk>/', ProductDeleteView.as_view(), name='delete_prod'),

    path('create_cat/', CategoryCreateView.as_view(), name='create_cat'),
    path('update_cat/<int:pk>/', CategoryUpdateView.as_view(), name='update_cat'),
    path('delete_cat/<int:pk>/', CategoryDeleteView.as_view(), name='delete_cat'),
]
