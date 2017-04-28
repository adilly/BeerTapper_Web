'''
Created on Apr 24, 2017

@author: Austin Dillinger
'''
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.base, name='base'),
    url(r'^core/$', views.core, name='core'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]