from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.base, name='base'),
    url(r'^core/$', views.core, name='core'),
    url(r'^index/$', views.index, name='index'),
]
