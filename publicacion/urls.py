# publicacion/urls.py
# coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    # /home/
    url(r'^$', view=views.IndexView.as_view()),
    url(r'^entrada/(?P<slug>[-\w]+)/$', view=views.EntradaDetailView.as_view()),

]