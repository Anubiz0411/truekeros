# publicacion/urls.py
# coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', view=views.IndexView.as_view()),
    url(r'^entrada/(?P<slug>[-\w]+)/$', view=views.EntradaDetailView.as_view()),
    url(r'^crear/', view=views.CrearPost.as_view()),

]