# home/urls.py
# coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    # /home/
    url(r'^$', view=views.index_view, name='home.index'),
]