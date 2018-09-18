from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.main),
    url(r'^[0-9]+/$', views.good),
]
