from django.urls import path, re_path
from . import views
import basketapp.views as basketapp

app_name = 'basket'

urlpatterns = [
    path(r'^$', basketapp.basket, name='view'),
    path('add/<int:pk>/', basketapp.basket_add, name='add'),
    path('remove/<int:pk>/', basketapp.basket_remove, name='remove'),
]
