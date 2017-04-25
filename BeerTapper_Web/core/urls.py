'''
Created on Apr 24, 2017

@author: Austin Dillinger
'''
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.core, name='core'),
]