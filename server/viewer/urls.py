from django.conf.urls import url
# from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sections$', views.sections, name='sections'),
    url(r'^requirements$', views.requirements, name='requirements'),
]
