# home/urls.py
# coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    # /home/
    url(r'^contact/$', view=views.ContactView.as_view(), name='home.contact'),
]