from django.conf.urls import include, url
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = [
        url(r'^add_image/$', views.upload_image_view , name='upload_image_view'),
        url(r'^post/new$', views.post_new , name='create_article'),
        url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    ]