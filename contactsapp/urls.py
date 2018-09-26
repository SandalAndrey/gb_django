from django.urls import path, re_path
from . import views

app_name = 'contacts'
urlpatterns = [
    re_path(r'^$', views.main, name='main'),
]
