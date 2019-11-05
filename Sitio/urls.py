from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import *


urlpatterns = [
	url(r'^$', views.portada, name='portada'),
    url('portada/', views.portada, name='portada'),
    path('nuevapublicacion/', views.nuevapublicacion, name='nuevapublicacion'),
    url('mispublicaciones/', views.mispublicaciones, name='mispublicaciones'),
    url(r'^verpublicacion/(?P<pk>[0-9]+)/$', views.verpublicacion, name='verpublicacion'),
	url(r'^editarpublicacion/(?P<pk>[0-9]+)/$', views.editarpublicacion, name='editarpublicacion'),
	url(r'^respondercomentario/(?P<pk>[0-9]+)/$', views.respondercomentario, name='respondercomentario'),
	url('errorpage/', views.errorpage, name='errorpage'),
	#url(r'dislike/(?P<pk>[0-9]+)/$', views.dislike, name='dislike')
]
