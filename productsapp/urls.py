from django.urls import path, re_path
from . import views

app_name = 'products'
urlpatterns = [
    re_path(r'^$', views.main, name='catalog'),
    path('<int:good_id>', views.good, name='detail'),
    path('category<int:cat_id>', views.main, name='category'),
]
