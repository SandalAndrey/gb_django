from django.urls import path, re_path
from productsapp.views import (product_create, main, good, category_update, category_create, category_delete, product_update, product_delete)

app_name = 'products'
urlpatterns = [
    path('create_prod/', product_create, name='create_prod'),
    path('update_prod/<int:pk>/', product_update, name='update_prod'),
    path('delete_prod/<int:pk>/', product_delete, name='delete_prod'),
    path('create_cat/', category_create, name='create_cat'),
    path('update_cat/<int:pk>/', category_update, name='update_cat'),
    path('delete_cat/<int:pk>/', category_delete, name='delete_cat'),
    re_path(r'^$', main, name='catalog'),
    path('<int:good_id>', good, name='detail'),
]
