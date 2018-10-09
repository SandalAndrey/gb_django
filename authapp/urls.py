from django.conf.urls import url

import authapp.views as authapp

app_name = 'auth'
urlpatterns = [
    url(r'^login/$', authapp.login, name='login'),
    url(r'^logout/$', authapp.logout, name='logout'),
]
